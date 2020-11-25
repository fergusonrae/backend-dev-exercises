"""Functions that require reading and writing disk data."""

import datetime
from pathlib import Path
import pickle
import sqlite3

import pandas as pd

from .constants import FLATTEN_SQL
from .model import SavedCSV
from .paths import DATA_DIR, SQLITE_DB

def flattened_exercise_to_csv() -> SavedCSV:
    """Using a specified set of tables and database, flatten the tables into a single table.
    Saves this table as a csv in the data directory of the project"""
    conn = sqlite3.connect(SQLITE_DB) # No need to disconnect, is handled by garbage collector
    flattened = pd.read_sql_query(FLATTEN_SQL, conn)
    return dataframe_to_csv(flattened, DATA_DIR)


def dataframe_to_csv(dataframe: pd.DataFrame, directory: Path) -> SavedCSV:
    """Saves a timestamped csv and its corresponding data map to the designated directory.
    Returns an object containing paths of both csv and datamap."""

    # Make the path a directory in case it is non-existent
    directory.mkdir(exist_ok=True, parents=True)

    # Collect paths
    timestamp = datetime.datetime.now().strftime('%m%d%Y-%H%M%S')
    data_map_path = directory / (timestamp + "_data_map.pkl")
    csv_path = directory / (timestamp + '_data.csv')

    data_map = dataframe.dtypes.to_dict()
    with data_map_path.open(mode='wb') as pkl_file:
        pickle.dump(data_map, pkl_file)
    dataframe.to_csv(csv_path, index=False)
    return SavedCSV(csv=csv_path, data_map=data_map_path)


def csv_to_dataframe(csv_path: SavedCSV) -> pd.DataFrame:
    """Takes csv and data_map and translate it into a pandas dataFrame."""
    with csv_path.data_map.open('rb') as pickle_file:
        data_map = pickle.load(pickle_file)
    return pd.read_csv(csv_path.csv, dtype=data_map)
