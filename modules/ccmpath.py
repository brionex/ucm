import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BIN_DIR = os.path.join(BASE_DIR, 'bin')
DATA_DIR = os.path.join(BASE_DIR, 'data')
