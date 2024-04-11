import os
import shutil
from pathlib import Path
import click
from const import CONST
from modules import ccmpath


@click.group(help=CONST.ucmd)
def ucmd():
    pass


@ucmd.command(help=CONST.ls)
def ls():
    cmds_list = os.listdir(ccmpath.BIN_DIR)
    max_len = len(max(cmds_list, key=len)) - 4

    print()
    for file_name in cmds_list:
        name, extension = os.path.splitext(file_name)

        if not extension == '.bat':
            continue

        # Lee el archivo bat para obtener la descripción del comando
        with open(os.path.join(ccmpath.BIN_DIR, file_name), "r", encoding="utf-8") as f:
            line = f.readline()

        print(f'  {name.ljust(max_len, ' ')} {line.replace('::', '')}', end='')
    print()


@ucmd.command(help=CONST.add)
@click.argument('name')
@click.option('-m', '--message', required=True, help=CONST.add_op)
def add(name, message):
    # Crea la carpeta para los comandos del usuario
    os.makedirs(ccmpath.DATA_DIR, exist_ok=True)

    bat_file = os.path.join(ccmpath.BIN_DIR, f'{name}.bat')
    py_file = os.path.join(ccmpath.DATA_DIR, name, f'{name}.py')

    # Verifica si ya existe el comando que se quiere crear
    if os.path.exists(bat_file):
        print(CONST.cmd_exist)
        return

    # Crea el archivo bat
    content_bat = os.path.join(Path(__file__).resolve().parent, 'content.txt')
    with open(content_bat, 'r', encoding="utf-8") as f:
        lines = f.read().format(message, name)
    with open(bat_file, 'w', encoding="utf-8") as f:
        f.write(lines)

    # Crea la carpeta y el archivo python principal
    os.makedirs(os.path.join(ccmpath.DATA_DIR, name), exist_ok=True)
    with open(py_file, 'w', encoding="utf-8") as f:
        f.write(CONST.py_content.format(name))
    print(CONST.cmd_created.format(name))


@ucmd.command(help=CONST.remove)
@click.argument('name')
def remove(name):
    bat_file = os.path.join(ccmpath.BIN_DIR, f'{name}.bat')
    data_folder = os.path.join(ccmpath.DATA_DIR, name)

    if not (os.path.exists(bat_file) and os.path.exists(data_folder)):
        print(CONST.cmd_not_exist)
        return

    res = input(CONST.confirm_remove.format(name))
    if res.lower() == 's':
        os.remove(bat_file)
        shutil.rmtree(data_folder)
        print(CONST.cmd_removed)
    else:
        print(CONST.remove_cancel)


if __name__ == "__main__":
    ucmd()
