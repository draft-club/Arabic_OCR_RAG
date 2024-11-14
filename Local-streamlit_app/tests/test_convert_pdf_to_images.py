import unittest
from unittest.mock import patch
from utils import convert_pdf_to_images


class TestConvertPdfToImages(unittest.TestCase):
    @patch('utils.convert_pdf_to_images')
    def test_convert_pdf_to_images(self, mock_convert):
        pdf_file_name = "sample.pdf"
        input_pdfs_path = "input_pdfs/"
        output_images_path = "output_images/"

        # Simulate return value
        mock_convert.return_value = ["image1.png", "image2.png"]

        result = convert_pdf_to_images(pdf_file_name, input_pdfs_path, output_images_path)

        # Assert that the result is a list of images
        self.assertEqual(result, ["image1.png", "image2.png"])
        mock_convert.assert_called_once_with(pdf_file_name, input_pdfs_path, output_images_path)


if __name__ == '__main__':
    unittest.main()
