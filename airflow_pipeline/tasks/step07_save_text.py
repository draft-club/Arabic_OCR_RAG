from utils import save_extracted_text
from task_decorator import task_logger


class SaveText:
    """Task to save extracted text to a file."""

    @staticmethod
    @task_logger
    def run(pdf_file_name, extracted_text, output_text_path):
        """Save extracted text to a file."""
        save_extracted_text(pdf_file_name, extracted_text, output_text_path)
