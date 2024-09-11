import sys
from pathlib import Path
from os import system
from shutil import copy, rmtree

from . import env
from .constants import Text
from .utils import compress_files
from .build import build
from .install import install


commands = {
    "ucm": "Ejecuta el CLI de 'ucm' en desarrollo",
    "clean": "Limpia la carpeta 'dev'",
    "build": "Genera los archivos compilados de la aplicación",
    "preview": "Ejecuta la aplicación compilada de CLI 'ucm'",
    "package": "Crea el paquete distribuible de la aplicación",
    "install": "Instala la aplicación en el sistema",
    "uninstall": "Desinstala la aplicación del sistema"
}


def info_cli():
    print("\nUso: run.py <comando>\n")
    for key, value in commands.items():
        print(f"  {key.ljust(10)} {value}")
    print()


def clean():
    rmtree(env.DEV_DIR)


def ucm():
    dev_json = env.DEV_DIR / "data.json"
    ucm_json = Path("src/data.json")
    ucm_path = Path("src/ucm.py")

    env.DEV_DIR.mkdir(parents=True, exist_ok=True)
    if not dev_json.exists():
        copy(ucm_json, dev_json)

    command = f"{env.PY_EXE} {ucm_path} {" ".join(sys.argv[2:])}"
    exit_code = system(command)
    if exit_code != 0:
        print(
            Text.cli_ucm_error.format(exit_code),
            file=sys.stderr
        )


def preview():
    app_exe = env.BUILD_APP / "dist" / "ucm" / "ucm.exe"

    if not app_exe.exists():
        print(Text.NO_APP_EXE)
        return

    command = f"{app_exe} {" ".join(sys.argv[2:])}"
    exit_code = system(command)

    if exit_code != 0:
        print(Text.PREVIEW_ERROR, file=sys.stderr)


def package():
    build()
    compress_files(
        [
            env.BUILD_APP / "dist" / "ucm" / "ucm.exe",
            env.BUILD_APP / "dist" / "ucm" / "data.json"
        ],
        env.RELEASE_DIR / "ucm.zip"
    )


def cli():
    args = sys.argv[1:]

    if not args:
        info_cli()
        return

    command = args[0]

    if command == "ucm":
        ucm()
        return

    if command == "build":
        build()
        return

    if command == "clean":
        clean()
        return

    if command == "preview":
        preview()
        return

    if command == "package":
        package()
        return

    if command == "install":
        install()
        return
