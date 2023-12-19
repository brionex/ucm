import sys
import os
from _modules.colors import C

n_args = len(sys.argv)

BASE = sys.argv[1]  # Ruta donde están ubicados los scripts.
COMMAND = sys.argv[2]
ARG_COMMAND = None

# Obtiene el comando del cual se va mostrar documentación.
if n_args == 4:
    ARG_COMMAND = sys.argv[3]


file_list = os.listdir(BASE)

# Clase que contiene las constantes utilizadas en el programa


class CONST:
    title = f'{C.CYAN}\nLista de comandos del Usuario.{C.R}'
    info = f'\n{C.CYAN}Para mas información sobre un comando.{C.R}\n - {COMMAND} <command>\n'
    not_doc = f'\n* No hay documentación del comando: {C.CYAN}{ARG_COMMAND}{C.R}\n'
    arg_error = f'\n* {C.RED}Argumentos proporcionados no válidos.{C.R}\n'
    not_exist = f'\n* {C.RED}El comando especificado no existe {C.R}\n'
    info_command = f'\nDocumentación del comando: {C.CYAN}{ARG_COMMAND}{C.R}\n'

# Función para mostrar la lista de comandos disponibles


def show_commands():
    print(CONST.title)

    for file in file_list:
        name, extension = os.path.splitext(file)
        if extension == '.bat':
            print(f' - {name}')

    print(CONST.info)

# Función para mostrar información sobre un comando específico


def show_info():
    # Verifica si se proporciona un nombre de archivo y si existe en la lista de archivos
    file_name = sys.argv[3] + '.bat'
    if file_name not in file_list:
        print(CONST.not_exist)
        return

    # Obtiene la ruta al archivo para mostrar su documentación
    path_file = os.path.join(BASE, file_name)

    # Abre el archivo y lee las líneas que comienzan con '::' para obtener la documentación
    with open(path_file, 'r') as file:
        lines = file.readlines()
        doc = [line.strip().replace('::', ' *')
               for line in lines if line.strip().startswith('::')]

        # Muestra la documentación si existe, de lo contrario, muestra un mensaje
        if doc:
            print(CONST.info_command)
            for text in doc:
                print(f'{text}')
            print()
        else:
            print(CONST.not_doc)


if __name__ == "__main__":
    # Verifica el número de argumentos proporcionados
    if n_args == 3:
        show_commands()
    elif n_args == 4:
        show_info()
    else:
        print(CONST.arg_error)
