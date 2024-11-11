from PIL import Image, ImageEnhance
import os
from task_decorator import task_logger


class EnhanceImages:
    """Task to enhance image quality by adjusting contrast."""

    @staticmethod
    @task_logger
    def run(image_files, output_images_path):
        """Enhance contrast of images."""
        enhanced_images = []
        for image_file in image_files:
            image = Image.open(os.path.join(output_images_path, image_file))
            enhancer = ImageEnhance.Contrast(image)
            enhanced_image = enhancer.enhance(1.5)  # Adjust contrast
            enhanced_images.append(enhanced_image)
        return enhanced_images
