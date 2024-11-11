import os
from utils import convert_pdf_to_images
from task_decorator import task_logger


class SavePDFAndConvertImages:
    """Task to save a PDF locally and convert it into images."""

    @staticmethod
    @task_logger
    def run(pdf_file_name, input_pdfs_path, output_images_path):
        """Save PDF and convert to images."""
        pdf_file_path = os.path.join(input_pdfs_path, pdf_file_name)
        image_files = convert_pdf_to_images(pdf_file_name, input_pdfs_path, output_images_path)
        return image_files
