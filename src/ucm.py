import click
from os import system

import env
from utils import Utils
from messages import Text

UTIL = Utils()


@click.group()
def cli():
    """
    Gestiona y organiza comandos personalizados del usuario, 
    facilitando su creación, ejecución y administración.
    """
    pass


@cli.command(name='list')
def ls():
    """Lista todos los comandos creados por el usuario"""
    click.echo(Text.ls_title)

    if not UTIL.json_cmds:
        click.echo(Text.empty_list)
        return

    for cmd, description in UTIL.json_cmds.items():
        name = cmd.ljust(UTIL.json_cmd_max + 2)
        click.echo(f' {click.style(name, fg="cyan")} {description}')
    click.echo()


@cli.command()
@click.argument('name')
def check(name):
    """Verifica si un comando existe en el sistema"""
    if UTIL.command_exists(name):
        click.secho(Text.check_exist.format(name), fg='green')
    else:
        click.secho(Text.check_not_exist.format(name), fg='yellow')


@cli.command()
@click.argument('name')
@click.option('-d', '--description', help=Text.add_option)
def add(name, description):
    """Crea los archivos para un nuevo comando"""
    if not UTIL.is_valid_name(name):
        click.secho(Text.invalid_name, fg="yellow")
        return

    if UTIL.command_exists(name):
        click.secho(Text.cmd_exist, fg='yellow')
        return

    UTIL.create_command_files(name)
    UTIL.json_cmds[name] = description
    UTIL.save_json()
    click.secho(Text.add_created.format(name), fg='green')


@cli.command()
@click.argument('command')
def remove(command):
    """Elimina un comando creado por el usuario"""
    if command not in UTIL.json_cmds:
        click.secho(Text.remove_not_exist, fg='red')
        return

    res = input(Text.remove_confirm.format(command))
    if res.lower() == 'y':
        UTIL.remove_command(command)
        click.secho(Text.remove_removed, fg='green')
    else:
        click.secho(Text.remove_cancel, fg='yellow')


@cli.command()
@click.argument('command')
@click.option('-n', '--name', help=Text.modify_name)
@click.option('-d', '--description', help=Text.modify_desc)
def modify(command, name, description):
    """Modifica el nombre o la descripción de un comando"""
    if command not in UTIL.json_cmds:
        click.secho(Text.modify_not_exist, fg='red')
        return

    if not name and not description:
        click.secho(Text.modify_not_option, fg='red')
        return

    if name:
        if not UTIL.is_valid_name(name):
            click.secho(Text.invalid_name, fg="yellow")
            return

        if UTIL.command_exists(name):
            click.secho(Text.cmd_exist, fg="yellow")
            return

    UTIL.modify_command(command, name, description)
    click.secho(Text.modify_modified, fg='green')


@cli.command(name='open')
@click.argument('command')
def open_command(command):
    """Abre el directorio de un comando en VS Code"""
    if command not in UTIL.json_cmds:
        click.secho(Text.open_not_exist, fg='yellow')
        return

    folder_path = env.DATA_DIR / command

    if not folder_path.exists():
        click.secho(Text.not_source_files, fg='red')
        return

    if folder_path.exists():
        try:
            command_str = f'code "{folder_path}"'
            click.echo(Text.open_files.format(command))
            result = system(command_str)

            if result == 0:
                click.echo(Text.open_success.format(command))
            else:
                click.secho(Text.open_error.format(result), fg='red')
        except Exception as e:
            click.secho(f"Error inesperado: {e}", fg='red')


if __name__ == '__main__':
    cli()
