import sys
import os


# sys.path.append(os.path.join(sys.argv[1], 'data'))
from _modules.colors import C


BASE = sys.argv[1]  # Ruta donde están ubicados los scripts.
COMMAND = sys.argv[2]
list_files = os.listdir(BASE)


class CONST:
    title = f'{C.CYAN}\nUser command list.{C.R}'
    info = f'\n{C.CYAN}For more information about a command.{
        C.R}\n - {COMMAND} <command>\n'
    not_doc = f'\nNo hay documentación sobre el comando: {COMMAND}.\n',
    arg_error = f'\n* {C.RED}Argumentos proporcionados no validos.{C.R}\n'


def show_commands():
    print(CONST.title)

    # Obtengo y recorro los archivos en la ubicación obtenida.
    for path in list_files:
        name, extension = os.path.splitext(path)
        if (extension in ['.bat']):
            print(f' - {name}')

    print(CONST.info)


def show_info():

    file_name = COMMAND + '.bat'

    if not file_name in list_files:
        print('no existe')
        return

    # Obtengo la ruta al archivo para mostrar su documentación.
    path_file = os.path.join(BASE, file_name)

    with open(path_file, 'r') as file:
        lines = file.readlines()
        doc = [line.strip() for line in lines if line.strip().startswith('::')]

    if (doc):
        print(f'\nInfo of command - {COMMAND}\n')
        for text in doc:
            print(f'{text.replace('::', ' *')}')
        print()
    else:
        print(CONST.not_doc)


if __name__ == "__main__":
    n_args = len(sys.argv)

    if n_args == 3:
        show_commands()
    elif n_args == 4:
        show_info()
    else:
        print(CONST.arg_error)
