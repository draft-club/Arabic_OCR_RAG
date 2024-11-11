from task_decorator import task_logger


class CropImages:
    """Task to crop images, removing header and footer."""

    @staticmethod
    @task_logger
    def run(enhanced_images, header_margin, footer_margin):
        """Crop images by removing headers and footers."""
        cropped_images = []
        for image in enhanced_images:
            cropped_image = image.crop((0, header_margin, image.width, image.height - footer_margin))
            cropped_images.append(cropped_image)
        return cropped_images
