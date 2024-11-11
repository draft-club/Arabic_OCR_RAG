import json
import os
import pandas as pd
from task_decorator import task_logger


class ExportData:
    """Task to export the extracted data to JSON and Excel formats."""

    @staticmethod
    @task_logger
    def run(df, output_text_path):
        """Export the DataFrame to both JSON and Excel formats."""
        # Save as JSON
        json_output = df.to_dict(orient="records")
        json_string = json.dumps(json_output, ensure_ascii=False, indent=4)
        json_file_path = os.path.join(output_text_path, "extracted_data.json")
        with open(json_file_path, 'w') as f:
            f.write(json_string)

        # Save as Excel
        excel_file_path = os.path.join(output_text_path, "extracted_data.xlsx")
        df.to_excel(excel_file_path, index=False)
