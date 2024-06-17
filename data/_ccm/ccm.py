import os
import sys
import shutil
from pathlib import Path
import click
from const import CONST
from func import *
from modules import env, lib


@click.group(help=CONST.ccm)
def ccm():
    pass


@ccm.command(help=CONST.list)
def list():
    cmd_list = get_cmds_doc()
    max_name = max(len(item['name']) for item in cmd_list)

    print()
    for cmd in cmd_list:
        name = cmd['name'].ljust(max_name + 2, ' ')
        print(f'  {name} {cmd["description"]}')
    print()


@ccm.command(help=CONST.add)
@click.argument('name')
@click.option('-d', '--description', required=True, help=CONST.add_op)
def add(name, description):
    bat_file = os.path.join(env.BIN_DIR, f'{name}.bat')
    py_file = os.path.join(env.DATA_DIR, name, f'{name}.py')
    cmd_list = get_cmds_list()

    # Valida si el nombre para el comando es valido.
    if not lib.validate_lowercase(name) and len(name) > 1:
        print(CONST.invalid_name)
        return

    # Verifica si ya existe el comando.
    if name in cmd_list or os.path.exists(bat_file):
        print(CONST.cmd_exist)
        return

    # Crea el archivo bat del comando.
    content_bat = os.path.join(env.DATA_DIR, '_ccm', 'content.txt')
    with open(content_bat, 'r', encoding="utf-8") as file:
        lines = file.read().format(name)
    with open(bat_file, 'w', encoding="utf-8") as file:
        file.write(lines)

    # Crea la carpeta en data y el archivo python principal del comando.
    os.makedirs(os.path.join(env.DATA_DIR, name), exist_ok=True)
    with open(py_file, 'w', encoding="utf-8") as file:
        file.write(CONST.py_content.format(name))
    print(CONST.cmd_created.format(name))

    # Agrega la información del nuevo comando al archivo doc.
    set_cmd_doc({'name': name, 'description': description})


@ccm.command(help=CONST.remove)
@click.argument('name')
def remove(name):
    bat_file = os.path.join(env.BIN_DIR, f'{name}.bat')
    data_folder = os.path.join(env.DATA_DIR, name)

    if name == 'ccm':
        print(CONST.cmd_remove_invalid)
        return

    if not name in get_cmds_list():
        print(CONST.cmd_not_exist)
        return

    # Verifica si existen los elementos a eliminar.
    if not (os.path.exists(bat_file) and os.path.exists(data_folder)):
        print(CONST.cmd_files_not_exist)
        return

    # Pide una confirmación y luego elimina el comando y sus datos.
    res = input(CONST.confirm_remove.format(name))
    if res.lower() == 'y':
        os.remove(bat_file)
        shutil.rmtree(data_folder)
        remove_cmd_doc(name)
        print(CONST.cmd_removed)
    else:
        print(CONST.remove_cancel)


# # ? Implementar este comando para:
# # ? - Modificar el nombre y descripción de un comando.
# # ? - Modifica la descripción.
# @ccm.command(help=CONST.modify)
# @click.argument('command')
# @click.option('-d', '--description', help=CONST.modify_desc)
# @click.option('-n', '--name', help=CONST.modify_name)
# def modify(command, description, name):
#     if not description and not name:
#         print(CONST.unspecified_option)
#         return

#     file_bat = os.path.join(ccmpath.BIN_DIR, command) + '.bat'

#     if not os.path.exists(file_bat):
#         print('el comando no existe')
#         return
#     if description:
#         print(file_bat)
#         print('Descripción modificada')
#     if name:
#         print('Nombre modificado')
if __name__ == "__main__":
    ccm()
