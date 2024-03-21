import os
import click
from colorama import Fore

BASE_PATH = os.environ['BASE_PATH']


@click.command()
def ucl():
    print('comando')
    pass


# @ucl.command(help='Lista los comandos del usuario.')
# def ls():
#     files_list = os.listdir(os.path.join(BASE_PATH, 'bin'))
#     print()
#     for file in files_list:
#         name, extension = os.path.splitext(file)
#         print(name)
#     print()


# @ucl.command()
# def comando2():
#     """Descripción del comando 2."""
#     click.echo('Ejecutando comando 2')


# @ucl.command()
# def comando3():
#     """Descripción del comando 3."""
#     click.echo('Ejecutando comando 3')


if __name__ == '__main__':
    ucl()


#   with open(file_path, 'w', encoding='utf-8') as file:
#     file.write(SCRIPT)


# # Especifica la ruta del archivo .bat que deseas crear
# archivo_bat = 'mi_script.bat'

# # Escribe el contenido en el archivo
# with open(archivo_bat, 'w') as archivo:
#     archivo.write(script_content)

# print(f'Se ha creado el archivo {archivo_bat}')
