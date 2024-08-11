import os
import click

# Ruta al archivo del historial
history_file = os.path.join(
    os.getenv('APPDATA'),
    'Microsoft',
    'Windows',
    'PowerShell',
    'PSReadLine',
    'ConsoleHost_history.txt'
)


def read_history():
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as file:
            return file.readlines()
    return []


def write_history(lines):
    with open(history_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)


@click.group()
def cli():
    pass


@cli.command(name='list')
def ls():
    """Lista todos los elementos del historial"""
    history = read_history()
    if history:
        print()
        for idx, line in enumerate(history):
            click.echo(f'{idx}. {line}', nl=False)
        print()
    else:
        click.echo('\nHistorial de comandos vacío\n')


@cli.command()
@click.argument('line_number', type=int)
def remove(line_number):
    """Elimina una línea específica del historial"""
    history = read_history()
    if 0 <= line_number < len(history):
        del history[line_number]
        write_history(history)
        click.echo(f'\nLínea {line_number} eliminada del historial.\n')
    else:
        click.echo('\nNúmero de línea fuera de rango.\n')


@cli.command()
def clear():
    """Elimina todo el historial."""
    if os.path.exists(history_file):
        os.remove(history_file)
        click.echo('\nSe ha borrado todo el historial.\n')
    else:
        click.echo('\nNo existe historial de la consola.\n')


@cli.command()
@click.argument('lines', nargs=-1)
def add(lines):
    """Agrega nuevos elementos al historial"""
    with open(history_file, 'a', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')
    click.echo('\nNuevos elementos agregados al historial.\n')


@cli.command()
def redup():
    """Elimina las líneas duplicadas del historial"""
    history = read_history()
    if history:
        write_history(list(set(history)))
        click.echo('\nSe han eliminado las líneas duplicadas del historial.\n')
    else:
        click.echo('\nNo hay historial para procesar.\n')


if __name__ == '__main__':
    cli()
