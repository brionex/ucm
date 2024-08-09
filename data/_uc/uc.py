import os
import shutil
from pathlib import Path
import click
from Texts import Text
import utils
from modules import env, lib


@click.group(help=Text.ccm)
def ccm():
    pass


@ccm.command(name='list', help=Text.ls)
def ls():
    """Muestra una lista de comandos con sus descripciones"""
    cmd_list = utils.load_cmds_doc()
    list_keys = cmd_list.keys()

    max_name = max(len(name) for name in list_keys)
    print(Text.ls_title)
    for cmd in list_keys:
        name = cmd.ljust(max_name + 2)
        print(f'  {click.style(name, fg='cyan')} {cmd_list[cmd]}')
    print()


@ccm.command(help=Text.check)
@click.argument('name')
def check(name):
    """Verifica si un comando existe en el sistema"""
    if utils.cmd_exists(name):
        click.secho(Text.check_exist.format(name), fg='green')
    else:
        click.secho(Text.check_not_exist.format(name), fg='yellow')


@ccm.command(help=Text.add)
@click.argument('name')
@click.option('-d', '--description', help=Text.add_option)
def add(name, description):

    if not lib.validate_lowercase(name) or len(name) < 2:
        click.secho(Text.invalid_name, fg="yellow")
        return

    if utils.cmd_exists(name):
        click.secho(Text.cmd_exist, fg='yellow')
        return

    # Prepara las rutas de los archivos a crear
    bat_file = Path(env.BIN_DIR) / f'{name}.cmd'
    py_file = Path(env.DATA_DIR) / name / f'{name}.py'
    template_path = Path(env.DATA_DIR) / '_ccm' / 'template_cmd.txt'

    # Crea el archivo cmd del comando
    with open(template_path, 'r', encoding="utf-8") as file:
        lines = file.read().format(name)
    with open(bat_file, 'w', encoding="utf-8") as file:
        file.write(lines)

    # Crea la carpeta en data y el archivo python principal del comando
    os.makedirs(Path(env.DATA_DIR) / name, exist_ok=True)
    with open(py_file, 'w', encoding="utf-8") as file:
        file.write(Text.py_content.format(name))
    print(Text.cmd_created.format(name))

    # Agrega la información del nuevo comando al archivo doc
    utils.add_cmd_doc({'name': name, 'description': description})


@ccm.command(help=Text.remove)
@click.argument('name')
def remove(name):
    if name == 'ccm':
        click.secho(Text.cmd_remove_invalid, fg='yellow')
        return

    if not name in utils.get_cmds_list_doc():
        click.secho(Text.cmd_not_exist, fg='yellow')
        return

    bat_file = Path(env.BIN_DIR) / f'{name}.cmd'
    data_folder = Path(env.DATA_DIR) / name

    # Pide una confirmación y luego elimina el comando y sus datos
    res = input(Text.confirm_remove.format(name))
    if res.lower() == 'y':
        os.remove(bat_file)
        shutil.rmtree(data_folder)
        utils.remove_cmd_doc(name)
        print(Text.cmd_removed)
    else:
        print(Text.remove_cancel)


# # ? Implementar este comando para:
# # ? - Modificar el nombre y descripción de un comando.
# # ? - Modifica la descripción.
# @ccm.command(help=Text.modify)
# @click.argument('command')
# @click.option('-d', '--description', help=Text.modify_desc)
# @click.option('-n', '--name', help=Text.modify_name)
# def modify(command, description, name):
#     if not description and not name:
#         print(Text.unspecified_option)
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
