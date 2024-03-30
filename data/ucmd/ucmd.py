import os
import shutil
import click


# Obtiene la ruta del directorio actual
current_dir = os.getcwd()



@click.group()
def ucmd():
    """Gestiona los comandos creados por el usuario"""


@ucmd.command()
def ls():
    """Lista todos los comandos disponibles"""
    cmd_folder = os.path.join(current_dir, 'bin')
    cmd_list = os.listdir(cmd_folder)
    max_len = len(max(cmd_list, key=len)) - 4

    print()
    for path in cmd_list:
        name, extension = os.path.splitext(path)
        if extension == '.bat':
            with open(os.path.join(cmd_folder, path), "r", encoding="utf-8") as f:
                linea = f.readline()
                print(f'  {name.ljust(max_len, ' ')} {
                      linea.replace('::', '')}', end='')
    print()


@ucmd.command()
@click.argument('name')
@click.option('-m', '--message', required=True, help='Agrega una descripción al comando')
def add(name, message):
    """Crea los archivos para un nuevo comando"""

    # Crea la carpeta para los comandos del usuario
    user_folder = os.path.join(current_dir, 'user')
    os.makedirs(user_folder, exist_ok=True)

    # Crea los archivos para implementar el comando
    command_bat = os.path.join(current_dir, 'bin', f'{name}.bat')
    command_folder = os.path.join(user_folder, name)
    command_py = os.path.join(user_folder, name, f'{name}.py')

    # Verifica si ya existe el comando que se quiere crear
    if os.path.exists(command_bat):
        print('\n  !Ya existe un comando con ese nombre\n')
        return

    # Crea el archivo bat.
    content_bat = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'content.txt'
    )

    with open(content_bat, 'r', encoding="utf-8") as f:
        content = f.read().format(message, name)

    with open(command_bat, 'w', encoding="utf-8") as f:
        f.write(content)

    # Crea la carpeta y el archivo python principal.
    os.makedirs(command_folder, exist_ok=True)
    with open(command_py, 'w', encoding="utf-8") as f:
        f.write(f'print("Ejecución del archivo {name}.py")')

    print(f'\n  Comando "{name}" creado con éxito.\n')


@ucmd.command()
@click.argument('name')
def remove(name):
    """Elimina un comando creado por el usuario"""

    bat_file = os.path.join(current_dir, 'bin', f'{name}.bat')
    data_folder = os.path.join(current_dir, 'user', name)

    exists_file = os.path.exists(bat_file)
    exists_folder = os.path.exists(data_folder)

    if exists_file and exists_folder:
        res = input(f'  Confirmar eliminar comando "{name}" (s): ')
        if res.lower() == 's':
            os.remove(bat_file)
            shutil.rmtree(data_folder)
            print('\n  !Comando eliminado con éxito\n')
        else:
            print('\n  Eliminación cancelada\n')
    else:
        print('\n  !El comando que deseas eliminar no existe\n')
        return


if __name__ == "__main__":
    ucmd()
