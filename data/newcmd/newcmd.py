import os
import click

# Obtiene la ruta del directorio actual
current_directory = os.getcwd()

@click.group()
def app():
    pass


@app.command()
# @app.argument('nuevo_comando', nargs=-1)
@app.option('-d', '--delete', help='Elemento a eliminar')
def newcmd(nuevo_comando, delete):
    if nuevo_comando:
        print(nuevo_comando)

    if delete:
        print('hola')

if __name__ == "__main__":
    app()
