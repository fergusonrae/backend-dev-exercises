
import pandas as pd

from data_read_write import dataframe_to_csv, csv_to_dataframe
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

def test_csv_to_dataframe(temp_dir):
    """Unit test for csv_to_dataframe(csv_path: SavedCSV) -> pd.DataFrame"""
    test_df = pd.DataFrame.from_dict({'string_col': ['01', '12'],
                                      'integer_col': [0, -15]})
    dir_to_save = temp_dir / 'saved_dir'
    saved_csv = dataframe_to_csv(test_df, dir_to_save)

    # Check that column types are imported correctly
    output = csv_to_dataframe(saved_csv)
    assert output.dtypes.to_dict() == {'string_col': object, 'integer_col': int}
