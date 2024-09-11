import os
import sys
import zipfile
import urllib.request
import subprocess
from pathlib import Path
import venv
import shutil
from .user_path import UserPath


# Recursos desde github y del proyecto local
github_res = 'url-github'
local_res = Path('release/ucm.zip')

# Rutas de instalación
i_folder = Path().home() / 'ucm-cli'
dest_zip = i_folder / 'ucm.zip'

is_exe = getattr(sys, 'frozen', False)


def install():

    i_folder.mkdir(exist_ok=True)

    if is_exe:
        # url_res = github_url
        # Descarga el archivo comprimido
        # print(f'Descargando {url}...')
        # urllib.request.urlretrieve(url, zip_path)
        # print('Descarga completa.')
        shutil.copy(local_res, dest_zip)
    else:
        shutil.copy(local_res, dest_zip)

    if dest_zip.exists():
        print('Descomprimiendo...')
        with zipfile.ZipFile(dest_zip, 'r') as zip_ref:
            zip_ref.extractall(i_folder)
        print('Descompresión completa.')

        # Elimina el archivo comprimido
        print('Eliminando archivo comprimido...')
        dest_zip.unlink()
        print('Archivo comprimido eliminado.')

    # Crea un entorno virtual de Python en la carpeta 'venv'
    print('Creando entorno virtual...')
    venv.create(i_folder / '.venv', with_pip=True)
    print('Entorno virtual creado.')

    bin_path = i_folder / 'bin'
    userpath = UserPath()
    userpath.put(str(i_folder), front=False)
    userpath.put(str(bin_path), front=False)

    # Ejemplo de uso
# if __name__ == "__main__":
#     user_path = UserPath()

#     # Añadir una nueva ubicación al final del PATH si no existe ya
#     location_to_add = "C:\\Program Files\\MyApp"
#     success = user_path.put(location_to_add, front=False)  # Añade al final
#     if success:
#         print(f"{location_to_add} se ha añadido correctamente al PATH.")
#     else:
#         print(f"No se pudo añadir {location_to_add} al PATH.")

#     # Verificar si una ubicación está en el nuevo PATH
#     location_to_check = "C:\\Program Files\\MyApp"
#     if user_path.location_in_new_path(location_to_check):
#         print(f"{location_to_check} está en el PATH.")
#     else:
#         print(f"{location_to_check} no está en el PATH.")

#     # Remover una ubicación del PATH
#     location_to_remove = "C:\\Program Files\\MyApp"
#     success = user_path.remove(location_to_remove)
#     if success:
#         print(f"{location_to_remove} se ha eliminado correctamente del PATH.")
#     else:
#         print(f"No se pudo eliminar {location_to_remove} del PATH.")
