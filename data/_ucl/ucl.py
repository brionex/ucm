import sys
import os
from _modules.colors import C

N_ARGS = len(sys.argv)
BASE = sys.argv[1]  # Ruta donde están ubicados los scripts.
ARG_COMMAND = None

# Obtiene el comando del cual se va mostrar documentación.
if N_ARGS == 3:
    ARG_COMMAND = sys.argv[2]

file_list = os.listdir(BASE)


# Clase que contiene las constantes utilizadas en el programa
class CONST:
    title = f'{C.CYAN}\nLista de comandos del Usuario.{C.R}'
    info = f'\n{C.CYAN}Para mas información sobre un comando.{C.R}\n - ucl <command>\n'
    command_doc = f'\nDocumentación del comando: {C.CYAN}{ARG_COMMAND}{C.R}\n'
    not_doc = f'\n* No hay documentación del comando: {C.CYAN}{ARG_COMMAND}{C.R}\n'
    args_error = f'\n* {C.RED}Argumentos proporcionados no válidos.{C.R}\n'
    not_exist = f'\n* {C.RED}El comando especificado no existe {C.R}\n'


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
    file_name = sys.argv[2] + '.bat'
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
            print(CONST.command_doc)
            for text in doc:
                print(f'{text}')
            print()
        else:
            print(CONST.not_doc)


if __name__ == "__main__":
    # Verifica el número de argumentos proporcionados
    if N_ARGS == 2:
        show_commands()
    elif N_ARGS == 3:
        show_info()
    else:
        print(CONST.args_error)
