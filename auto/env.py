from pathlib import Path

VENV_SCRIPTS = Path(".venv/Scripts")
PY_EXE = VENV_SCRIPTS / "python"
PY_INSTALLER = VENV_SCRIPTS / "pyinstaller.exe"

APP_DIR = Path("src")
APP_FILE = APP_DIR / "ucm.py"
APP_JSON = APP_DIR / "data.json"

BUILD_DIR = Path("build")
DEV_DIR = BUILD_DIR / "dev"
BUILD_APP = BUILD_DIR / "app"
RELEASE_DIR = Path("release")
