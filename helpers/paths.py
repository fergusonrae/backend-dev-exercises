
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SQLITE_DB = PROJECT_ROOT / 'exercise01.sqlite'
DATA_DIR = PROJECT_ROOT / 'data'

# Saved data
SAVED_CSV_PATH = DATA_DIR / '11242020-210304_data.csv'
SAVED_DATA_MAP = DATA_DIR / '11242020-210304_data_map.pkl'
