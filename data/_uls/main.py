import sys, os
import colors

print(sys.argv)

BASE = sys.argv[1] # Ruta donde están ubicados los scripts.
COMMAND = sys.argv[2]
list_files = os.listdir(BASE)

class CONST:
    title = '\nUser command list.'
    info = f'\nFor more information about a command.\n - {sys.argv[2]} <command>\n'
    not_doc = f'\nNo hay documentación sobre el comando: {sys.argv[4]}.\n'



def show_commands():
    print(CONST.title)

    # Obtengo y recorro los archivos en la ubicación obtenida.
    for path in list_files:
        name, extension = os.path.splitext(path)
        if (extension in ['.bat']): print(f' - {name}')
        
    print(CONST.info)



def show_info():

    file_name = sys.argv[2] + '.bat'

    if not file_name in list_files:
        print('no existe')
        return 


    # Obtengo la ruta al archivo para mostrar su documentación.
    path_file = os.path.join(BASE, file_name)

    with open(path_file, 'r') as file:
        lines = file.readlines()
        doc = [line.strip() for line in lines if line.strip().startswith('::')]

    if (doc):
        print(f'\nInfo of command - {sys.argv[2]}\n')
        for text in doc:
            print(f'{text.replace('::', ' *')}')
        print()
    else:
        print(CONST.not_doc)

    








if __name__ == "__main__":
    num_args = len(sys.argv)

    if num_args == 3: show_commands()
    elif num_args == 4: show_info()
    else:
        print('Los argumentos adicionales no son validos.')
