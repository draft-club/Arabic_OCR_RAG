from config import load_config
from tasks.save_pdf_and_convert_to_images import SavePDFAndConvertImages
from tasks.enhance_images import EnhanceImages
from tasks.crop_images import CropImages
from tasks.detect_tables import DetectTables
from tasks.merge_tables import MergeTables
from tasks.extract_text import ExtractText
from tasks.save_text import SaveText
from tasks.extract_fields_using_llm import ExtractFieldsUsingLLM
from tasks.export_data import ExportData


class MainPipeline:
    """Main pipeline orchestration for the OCR and LLM tasks."""

    def __init__(self, pdf_file_name):
        self.pdf_file_name = pdf_file_name
        self.config = load_config()

    def run_pipeline(self):
        # Task 1: Save PDF and Convert to Images
        image_files = SavePDFAndConvertImages.run(self.pdf_file_name, self.config['input_pdfs_path'],
                                                  self.config['output_images_path'])

        # Task 2: Enhance Images
        enhanced_images = EnhanceImages.run(image_files, self.config['output_images_path'])

        # Task 3: Crop Images (Remove header and footer)
        cropped_images = CropImages.run(enhanced_images, self.config["header_margin"], self.config["footer_margin"])

        # Task 4: Detect Tables
        table_output = DetectTables.run(cropped_images)

        # Task 5: Merge Tables into DataFrame
        df = MergeTables.run(table_output)

        # Task 6: Extract Text from Images
        extracted_text = ExtractText.run(image_files, self.config['output_images_path'], self.config)

        # Task 7: Save Extracted Text
        SaveText.run(self.pdf_file_name, extracted_text, self.config['output_text_path'])

        # Task 8: Extract Fields using LLM
        llm_df = ExtractFieldsUsingLLM.run(extracted_text)

        # Task 9: Export Data to JSON and Excel
        ExportData.run(llm_df, self.config['output_text_path'])


if __name__ == "__main__":
    # Specify your PDF file name here
    pdf_file_name = "your_pdf_file.pdf"
    pipeline = MainPipeline(pdf_file_name)
    pipeline.run_pipeline()
