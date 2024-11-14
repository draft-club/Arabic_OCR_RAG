import unittest
from tasks.merge_tables import MergeTables
import pandas as pd

class TestMergeTables(unittest.TestCase):
    def test_merge_tables(self):
        output = {"table": [["header1", "header2"], ["row1", "row2"]]}

        df = MergeTables.run(output)

        # Check if the result is a DataFrame and if it has expected content
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertEqual(df.columns.tolist(), ["header1", "header2"])
        self.assertEqual(df.iloc[0].tolist(), ["row1", "row2"])

if __name__ == '__main__':
    unittest.main()
