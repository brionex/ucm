# pylint: disable=W0718

import os
import shutil
import click


filename = 'eslintrc.json'

current_dir = os.path.dirname(os.path.abspath(__file__))
destination_dir = os.getcwd()

eslint_file = os.path.join(current_dir, filename)
destination_file_dir = os.path.join(destination_dir, filename)


def copy_file():
    try:
        shutil.copy2(eslint_file, destination_file_dir)
        click.echo(f'\nArchivo copiado a: {destination_file_dir}\n')
    except Exception as e:
        click.echo(f'\nError al copiar el archivo: {e}\n')


@click.command()
def eslint():
    """
    Copia el archivo .eslintrc.json desde la misma carpeta que el script
    al directorio actual.
    """

    if not os.path.isfile(eslint_file):
        click.secho(
            f'\n!El archivo de configuración {filename} no existe\n',
            fg='yellow'
        )
        return

    if os.path.isfile(destination_file_dir):
        click.echo(f'\nEl archivo {filename} ya existe en la ruta actual')
        res = click.prompt(
            '¿Deseas sobrescribir? (s/n)',
            type=str
        ).strip().lower()

        if res == 's':
            copy_file()
        else:
            click.echo('\nOperación cancelada\n')
        return

    copy_file()


if __name__ == '__main__':
    eslint()
