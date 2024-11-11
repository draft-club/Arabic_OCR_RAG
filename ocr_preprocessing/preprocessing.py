from PIL import Image, ImageEnhance


def preprocess_image(image, config):
    """
    Preprocesses the image by enhancing contrast and removing header/footer.
    """
    # Enhance image contrast
    enhancer = ImageEnhance.Contrast(image)
    contrast_factor = 1.5
    image = enhancer.enhance(contrast_factor)

    # Crop image to remove header and footer
    header_margin = config["header_margin"]
    footer_margin = config["footer_margin"]
    image = image.crop((0, header_margin, image.width, image.height - footer_margin))

    return image

def process_pdf(pdf_file, config):
    """
    Processes a single PDF file: converts it to images,
    extracts tables, and applies enhancements.
    """
    output = {"text": "to implement later", "table": []}
    first_table_found = False
    page_number = 1

    # Convert the PDF into images
    image_files = convert_pdf_to_images(pdf_file, INPUT_PDFS_PATH, OUTPUT_IMAGES_PATH)

    for image_file in image_files:
        image_path = OUTPUT_IMAGES_PATH + image_file
        print(f"Processing page {page_number} from {pdf_file}")

        # Open and enhance the image
        image = Image.open(image_path)
        image = preprocess_image(image, config)

        # Extract tables from the image
        tables = extract_tables_from_image_as_dict(image, language="ara")
        table_found = bool(tables)

        # Check for new table structure or end of table
        if table_found:
            num_columns = len(tables[0]["table_dict"][0])
            if not first_table_found:
                first_table_found = True
                num_columns_first = num_columns
            elif num_columns != num_columns_first:
                print("New table structure found, stopping further extraction.")
                break  # A new table structure indicates the end of the previous table
        elif first_table_found:
            print("Page without table, stopping further extraction.")
            break  # No table after the first indicates the end of extraction
        else:
            print("No table detected yet.")
            continue

        # Append the table data to the output
        for table in tables:
            table_dict = table["table_dict"]
            output["table"].extend(table_dict.values())

        page_number += 1
        if page_number == 8:  # Limit processing to 8 pages for now
            break

    return output

def preprocess_image(image, config):
    """
    Preprocesses the image by enhancing contrast and removing header/footer.
    """
    # Enhance image contrast
    enhancer = ImageEnhance.Contrast(image)
    contrast_factor = 1.5
    image = enhancer.enhance(contrast_factor)

    # Crop image to remove header and footer
    header_margin = config["header_margin"]
    footer_margin = config["footer_margin"]
    image = image.crop((0, header_margin, image.width, image.height - footer_margin))

    return image


