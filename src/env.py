from pathlib import Path
import sys

# Rutas en modo desarrollo
BASE_DIR = Path(__file__).parent.parent / 'build' / 'dev'
VENV_PY = Path('../../.venv/Scripts/python.exe')
JSON_PATH = BASE_DIR / 'data.json'
BIN_DIR = BASE_DIR / 'bin'
DATA_DIR = BASE_DIR / 'data'

# Rutas para el archivo ejecutable
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
    VENV_PY = Path('.venv/Scripts/python.exe')
    JSON_PATH = BASE_DIR / 'data.json'
    BIN_DIR = BASE_DIR / 'bin'
    DATA_DIR = BASE_DIR / 'data'
