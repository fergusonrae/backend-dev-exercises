
from dataclasses import dataclass
from pathlib import Path

@dataclass
class SavedCSV:
    """Object to access the paths of data saved in order to generate a csv file."""
    csv: Path
    data_map: Path