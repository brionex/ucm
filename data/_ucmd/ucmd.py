import os
import click
from colors import Colors


BASE_PATH = os.environ['BASE']

colors = Colors()

print(colors.apply('red::hola'))

const = colors.apply({
    'main': 'cyan::ucmd - Crea, lista y elimina comandos.'
})




@click.group(help=const.main)
def ucmd():
    """Comando principal."""


@ucmd.command()
def comando1():
    """Descripción del comando 1."""
    click.echo('Ejecutando comando 1')


@ucmd.command()
def comando2():
    """Descripción del comando 2."""
    click.echo('Ejecutando comando 2')


@ucmd.command()
def comando3():
    """Descripción del comando 3."""
    click.echo('Ejecutando comando 3')


if __name__ == '__main__':
    ucmd()


#   with open(file_path, 'w', encoding='utf-8') as file:
#     file.write(SCRIPT)


# # Especifica la ruta del archivo .bat que deseas crear
# archivo_bat = 'mi_script.bat'

# # Escribe el contenido en el archivo
# with open(archivo_bat, 'w') as archivo:
#     archivo.write(script_content)

# print(f'Se ha creado el archivo {archivo_bat}')
