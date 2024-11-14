import unittest
from PIL import Image
from unittest.mock import patch, MagicMock
from tasks.enhance_images import EnhanceImages

class TestEnhanceImages(unittest.TestCase):
    @patch('PIL.Image.open')
    def test_enhance_images(self, mock_image_open):
        # Mock image processing
        mock_image = MagicMock()
        mock_image_open.return_value = mock_image

        image_files = ["image1.png", "image2.png"]
        output_images_path = "output_images/"

        result = EnhanceImages.run(image_files, output_images_path)

        # Check if enhancement was called
        mock_image_open.assert_called()
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
