# pylint: disable=E1120
# pylint: disable=W0622
# pylint: disable=W0718

import os
import shutil
import click


def remove_pycache(root_dir):
    click.echo(f'Buscando __pycache__ en: {root_dir}')
    for dirpath, dirnames, _ in os.walk(root_dir):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                click.echo(f'Removido: {pycache_path}')
            except Exception as e:
                click.echo(f'Error al eliminar {pycache_path}: {e}')


@click.command()
@click.argument('dir', type=click.Path(exists=True, file_okay=False))
def cli(dir):
    """
    CLI para eliminar __pycache__ en el directorio especificado.

    :param dir: El directorio específico donde buscar y eliminar __pycache__.
    """
    click.echo(f'\nIniciando eliminación en: {dir}')
    remove_pycache(dir)


if __name__ == '__main__':
    cli()
