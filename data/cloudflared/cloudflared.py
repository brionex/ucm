# pylint: disable=E1120

import subprocess
import os
import click


@click.command()
@click.argument('url', type=str)
def start_tunnel(url):
    """
    Inicia un túnel Cloudflare con la URL proporcionada.

    :param url: La URL local que deseas exponer a través del túnel.
    """
    # Obtén la ruta del directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construye la ruta completa al ejecutable
    exe_path = os.path.join(current_dir, 'cloudflared-windows-amd64.exe')

    # Comando para ejecutar el archivo
    command = [exe_path, '--url', url]

    try:
        # Ejecuta el comando
        subprocess.run(command, check=True)
        click.echo(f'Túnel iniciado con URL: {url}')
    except subprocess.CalledProcessError as e:
        click.echo(f'Error al ejecutar el comando: {e}')
    except FileNotFoundError:
        click.echo(
            'El archivo ejecutable no se encuentra en la ruta especificada.')


if __name__ == '__main__':
    start_tunnel()
