import os
import shutil
from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
)
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embedding import get_embedding_function
from langchain_community.vectorstores import Chroma
from paths import OUTPUT_TEXT_PATH

CHROMA_PATH = "chroma"
DATA_PATH = OUTPUT_TEXT_PATH


class CustomTextFileLoader:
    """Custom loader for text files."""
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return [Document(page_content=content, metadata={"source": self.file_path})]
        except Exception as e:
            print(f"Error loading text file {self.file_path}: {e}")
            return []


def load_documents():
    documents = []

    # Load all files in the directory
    for root, _, files in os.walk(DATA_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1].lower()

            # Match loader to file extension
            try:
                if extension == ".pdf":
                    loader = PyPDFLoader(file_path)
                    documents.extend(loader.load())
                elif extension == ".txt":
                    loader = CustomTextFileLoader(file_path)
                    documents.extend(loader.load())
                elif extension == ".csv":
                    loader = CSVLoader(file_path)
                    documents.extend(loader.load())
                else:
                    print(f"Unsupported file type: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    return documents


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


def add_to_chroma(chunks: list[Document]):
    # Load the existing database.
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        print("✅ No new documents to add")


def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page", 0)
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page metadata.
        chunk.metadata["id"] = chunk_id

    return chunks


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
        print("Database cleared.")
    else:
        print("No database found to clear.")



