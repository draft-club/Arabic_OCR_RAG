from textify_docs.tables.table_extracter import extract_tables_from_image_as_dict
from task_decorator import task_logger


class DetectTables:
    """Task to detect tables from images."""

    @staticmethod
    @task_logger
    def run(cropped_images):
        """Detect tables in the cropped images."""
        output = {"text": "To implement later", "table": []}
        first_table_found = False
        for page, image in enumerate(cropped_images):
            tables = extract_tables_from_image_as_dict(image, language="ara")
            if tables:
                for table in tables:
                    table_dict = table["table_dict"]
                    for row in table_dict.values():
                        output["table"].append(row)
            else:
                if first_table_found:
                    break
        return output
