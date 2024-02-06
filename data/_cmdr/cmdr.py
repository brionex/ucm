'''
Script: cmdr

'''

import sys
import os
from lib import validate_folder_name

SCRIPT = r'''@echo off
set "dirname=%~dp0"
set "venvpy=%dirname%..\data\_venv\Scripts\python.exe"
%venvpy% "%dirname%..\data\_cmdr\cmdr.py" %*
'''

def main():
  args = sys.argv[1:]
  base_path = os.path.abspath(os.path.join(__file__, '../../..'))

  file_path = os.path.join(base_path, 'bin', f'{args[1]}.bat')

  if args[0] == 'new' and validate_folder_name(args[1]):
    if os.path.exists(file_path):
      print('Archivo ya existe')
    else:
      with open(file_path, 'w', encoding='utf-8') as file:
        file.write(SCRIPT)





if __name__ == "__main__":
  main()






# # Especifica la ruta del archivo .bat que deseas crear
# archivo_bat = 'mi_script.bat'

# # Escribe el contenido en el archivo
# with open(archivo_bat, 'w') as archivo:
#     archivo.write(script_content)

# print(f'Se ha creado el archivo {archivo_bat}')
