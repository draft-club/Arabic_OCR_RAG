from utils import extract_text_from_images
from task_decorator import task_logger


class ExtractText:
    """Task to extract text from images."""

    @staticmethod
    @task_logger
    def run(image_files, output_images_path, config):
        """Extract text from images using OCR."""
        extracted_text = extract_text_from_images(image_files, output_images_path, config)
        return extracted_text
