import os
import click

os.system('cls')  # ! Borrar al terminar !!!!


# Obtiene la ruta del directorio actual
current_directory = os.getcwd()


@click.command()
@click.argument('name')
@click.option('--delete', '-d', is_flag=True, help='Elimina un comando del usuario')
@click.option('--rename', '-r', help='Renombra un comando del usuario')
@click.pass_context
def newcmd(ctx, name, delete, rename):
    """
    Este comando crea los archivos para la implementación de un nuevo
    comando personalizado del usuario.
    """

    if delete:
        print('delete')
    elif rename:
        print('rename')
    elif name:
        print('name')
    else:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    newcmd()
