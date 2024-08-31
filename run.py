import os
import sys
import subprocess


def create_virtualenv():
    """Crea un entorno virtual en la carpeta '.venv'."""
    if not os.path.exists('.venv'):
        print("\nCreando el entorno virtual...")
        subprocess.check_call([sys.executable, '-m', 'venv', '.venv'])
        print("Entorno virtual creado.")
    else:
        print("\nEl entorno virtual ya existe.\n")


def install_dependencies():
    """Instala las dependencias en el entorno virtual."""
    print("Instalando dependencias...\n")
    subprocess.check_call(
        [os.path.join('.venv', 'Scripts', 'pip'), 'install', '-r', 'requirements.txt'])
    print("\nDependencias instaladas.")


if __name__ == "__main__":
    if 'setup' in sys.argv:
        create_virtualenv()
        install_dependencies()
        print("Entorno de desarrollo listo.\n")
        exit()
