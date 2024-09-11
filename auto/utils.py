from zipfile import ZipFile
from pathlib import Path

from .constants import Text


def compress_files(files, zip_file):
    print(Text.build_zip_start)
    """Comprime archivos en un ZIP."""
    with ZipFile(zip_file, "w") as zipf:
        for file in files:
            zipf.write(file, arcname=Path(file).name)
    print(Text.build_zip_end)
