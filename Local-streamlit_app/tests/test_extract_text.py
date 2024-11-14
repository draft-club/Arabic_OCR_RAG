import unittest
from unittest.mock import patch
from utils import extract_text_from_images

class TestExtractText(unittest.TestCase):
    @patch('utils.extract_text_from_images')
    def test_extract_text_from_images(self, mock_extract_text):
        image_files = ["image1.png", "image2.png"]
        output_images_path = "output_images/"
        config = {"config_key": "config_value"}

        # Simulate the text extraction
        mock_extract_text.return_value = "Sample extracted text"

        result = extract_text_from_images(image_files, output_images_path, config)

        # Assert the returned text
        self.assertEqual(result, "Sample extracted text")
        mock_extract_text.assert_called_once_with(image_files, output_images_path, config)

if __name__ == '__main__':
    unittest.main()
