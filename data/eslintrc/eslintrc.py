import os
import sys
from colors import Colors


CONST = Colors({
    'file': 'eslintrc.json',
    'origin_error': '\n* {lightRed}Error con el archivo de origen.\n'
})

destination_path = sys.argv[2]

file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    CONST.file
)

print(CONST.file)

if not os.path.exists(file): 
    print(CONST.origin_error)
    exit()




