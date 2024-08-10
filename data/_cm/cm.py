from pathlib import Path
import subprocess
import click
import utils
from Texts import Text
from modules import lib


json_data = utils.load_json()


@click.group()
def cli():
    """Gestiona los comandos creados por el usuario"""


@cli.command(name='list')
def ls():
    """Lista todos los comandos creados por el usuario"""
    cmd_list = json_data['cmds']
    max_name = max(len(name) for name in cmd_list)

    click.echo(Text.ls_title)
    for cmd, desc in cmd_list.items():
        name = cmd.ljust(max_name + 2)
        click.echo(f'  {click.style(name, fg="cyan")} {desc}')
    click.echo()


@cli.command()
@click.argument('name')
def check(name):
    """Verifica si un comando ya existe en el sistema"""
    if not lib.validate_lowercase(name) or len(name) < 2:
        click.secho(Text.invalid_name, fg="yellow")
        return

    if utils.command_exists(name):
        click.secho(Text.check_exist.format(name), fg='green')
    else:
        click.secho(Text.check_not_exist.format(name), fg='yellow')


@cli.command()
@click.argument('name')
@click.option('-d', '--description', help=Text.add_option)
def add(name, description):
    """Crea los archivos para un nuevo comando"""
    if not lib.validate_lowercase(name) or len(name) < 2:
        click.secho(Text.invalid_name, fg="yellow")
        return

    if utils.command_exists(name):
        click.secho(Text.cmd_exist, fg='yellow')
        return

    # Crear archivos necesarios
    utils.create_command_files(name, json_data['cmd_template'].format(name))

    # Actualizar JSON
    json_data['cmds'][name] = description
    utils.save_json(json_data)
    click.secho(Text.add_created.format(name), fg='green')


@cli.command()
@click.argument('command')
def remove(command):
    """Elimina un comando creado por el usuario"""
    if command == 'cm':
        click.secho(Text.remove_invalid, fg='yellow')
        return

    if command not in json_data['cmds']:
        click.secho(Text.remove_not_exist, fg='yellow')
        return

    res = input(Text.remove_confirm.format(command))
    if res.lower() == 'y':
        utils.remove_command(command, json_data)
        click.secho(Text.remove_removed, fg='green')
    else:
        click.secho(Text.remove_cancel, fg='yellow')


@cli.command()
@click.argument('command')
@click.option('-n', '--name', help=Text.modify_name)
@click.option('-d', '--description', help=Text.modify_desc)
def modify(command, name, description):
    """Modifica el nombre o la descripción de un comando"""
    if command == 'cm':
        click.secho(Text.modify_invalid, fg='yellow')
        return

    if command not in json_data['cmds']:
        click.secho(Text.modify_not_exist, fg='yellow')
        return

    if not name and not description:
        click.secho(Text.modify_not_option, fg='yellow')
        return

    if name:
        if not lib.validate_lowercase(name) or len(name) < 2:
            click.secho(Text.invalid_name, fg="yellow")
            return

        if utils.command_exists(name):
            click.secho(Text.cmd_exist, fg="yellow")
            return

    utils.modify_command(command, name, description, json_data)
    click.secho(Text.modify_modified, fg='green')


@cli.command(name='open')
@click.argument('command')
def open_command(command):
    """Abre el directorio de un comando en vscode"""
    if command == 'cm':
        click.secho(Text.open_invalid, fg='yellow')
        return

    if command not in json_data['cmds']:
        click.secho(Text.open_not_exist, fg='yellow')
        return

    folder_path = Path(utils.env.DATA_DIR) / command

    if folder_path.exists():
        try:
            subprocess.run(['code', str(folder_path)], check=True, shell=True)
            click.echo(Text.open_success.format(command))
        except subprocess.CalledProcessError as e:
            click.secho(Text.open_error.format(e), fg='yellow')
        except FileNotFoundError:
            click.secho(Text.open_not_vscode, fg='yellow')


if __name__ == '__main__':
    cli()
