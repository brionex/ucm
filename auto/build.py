import subprocess
from shutil import copy, rmtree

from . import env
from .constants import Text


def build():
    """
    Construye el ejecutable usando PyInstaller y comprime en
    un ZIP los archivos necesarios para su distribución.
    """

    # Verifica que los caminos requeridos existan
    if not env.PY_INSTALLER.exists():
        print(Text.PYINSTALLER_MISSING)
        return False

    if not env.RELEASE_DIR.exists():
        print(Text.NO_RELEASE_FOLDER)
        return False

    print(Text.BUILD_START)
    if env.BUILD_APP.exists():
        rmtree(env.BUILD_APP)

    # Configuración del comando de PyInstaller
    commands = [
        env.PY_INSTALLER,
        "--onedir",
        "--distpath", env.BUILD_APP / "dist",
        "--workpath", env.BUILD_APP / "temp",
        "--specpath", env.BUILD_APP / "spec",
        env.APP_FILE
    ]

    # Ejecuta el comando de construcción
    try:
        print(Text.PACKAGING_APP)
        result = subprocess.run(
            commands,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Subprocess result:", result.stdout)
        print(Text.PACKAGING_DONE)
    except subprocess.CalledProcessError as e:
        print(f"Error en la construcción: {e.stderr}")
        return False

    print(Text.COLLECT_ADDITIONAL)
    copy(env.APP_JSON, env.BUILD_APP / "dist" / "ucm" / "data.json")
    print(Text.BUILD_END)
