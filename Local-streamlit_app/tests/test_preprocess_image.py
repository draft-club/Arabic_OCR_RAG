import unittest
from unittest.mock import patch
from ocr_preprocessing.preprocessing import preprocess_image


class TestPreprocessImage(unittest.TestCase):
    @patch('ocr_preprocessing.preprocessing.preprocess_image')
    def test_preprocess_image(self, mock_preprocess):
        image_path = "path/to/image.png"

        # Simulate preprocessing output
        mock_preprocess.return_value = "processed_image.png"

        result = preprocess_image(image_path)

        # Assert that the result matches the processed image
        self.assertEqual(result, "processed_image.png")
        mock_preprocess.assert_called_once_with(image_path)


if __name__ == '__main__':
    unittest.main()
