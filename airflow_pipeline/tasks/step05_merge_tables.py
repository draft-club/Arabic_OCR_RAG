import pandas as pd
from task_decorator import task_logger


class MergeTables:
    """Task to merge tables into a DataFrame."""

    @staticmethod
    @task_logger
    def run(output):
        """Merge extracted tables into a Pandas DataFrame."""
        if output["table"]:
            df = pd.DataFrame(output["table"][1:], columns=output["table"][0])
        else:
            df = pd.DataFrame()
        return df
