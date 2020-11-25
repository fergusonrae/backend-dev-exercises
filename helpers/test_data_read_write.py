
import pandas as pd

from data_read_write import dataframe_to_csv
from model import SavedCSV

def test_dataframe_to_csv(temp_dir):
    """Unit test for dataframe_to_csv(dataframe: pd.DataFrame, directory: Path) -> SavedCSV"""

    # Create test df that contains string items that will convert to int if dtype is not specified
    # Directory to save to has multiple layers of non-existent folders. Assert it can still be created.
    test_df = pd.DataFrame.from_dict({'string_col': ['01', '12'],
                                      'integer_col': [0, -15]})
    output_dir = temp_dir / 'empty' / 'dirs'
    assert not output_dir.is_dir()
    output = dataframe_to_csv(test_df, output_dir)
    assert isinstance(output, SavedCSV)
    assert output.csv.is_file()
    assert output.data_map.is_file()
