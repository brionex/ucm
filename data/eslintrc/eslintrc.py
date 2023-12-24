from os import path
import sys
import shutil
from colors import Colors


CONST = Colors({
    'file': 'eslintrc.json',
    'origin_error': '\n{lightRed} !Error con el archivo de origen.\n',
    'exist': '\nEl archivo ya existe en la ruta:',
    'generated': '\nArchivo generado en la ruta actual:'
})

# Obtiene la ruta del archivo base y la ruta de destino.
base_file = path.join(
    path.dirname(path.abspath(__file__)), 
    CONST.file
)
destination_path = path.join(sys.argv[2], CONST.file)

# Comprueba si existe el archivo de origen.
if not path.exists(base_file): 
    print(CONST.origin_error)
    exit()

# Comprueba si el archivo ya existe en la ruta de destino.
if path.exists( destination_path ):
    print(CONST.exist)
    print(Colors(f'{{yellow}}{destination_path}\n'))
    exit()

# Copia el archivo base a la ruta de destino.
shutil.copy(base_file, destination_path)
print(CONST.generated)
print(Colors(f'{{yellow}}{destination_path}\n'))


