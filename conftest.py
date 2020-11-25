
from pathlib import Path
import shutil
import tempfile

import pytest

@pytest.fixture(scope='module')
def temp_dir():
    """Creates a directory to store testing files and then once the module is done with it
    deletes all contents"""
    temp_dir_path = Path(tempfile.mkdtemp())
    yield temp_dir_path
    shutil.rmtree(temp_dir_path)
