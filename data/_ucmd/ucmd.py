'''
Script: cmdr

'''

import sys
import os
from lib import validate_folder_name

BASE_PATH = os.path.abspath(os.path.join(__file__, '../../..'))



def generate_bat_script(name):
  content = r'''@echo off
  set "dirname=%~dp0"
  set "venvpy=%dirname%..\data\_venv\Scripts\python.exe"
  %venvpy% "%dirname%..\data\_cmdr\cmdr.py" %*
  '''





def main():
  args = sys.argv[1:]

  # file_path = os.path.join(base_path, 'bin', f'{args[1]}.bat')
  if len(args) == 0:
    print('0000')
    return


  if args[0] == 'new' and validate_folder_name(args[1]):
    print('hola')
    
    # if os.path.exists(file_path):
    #   print('Archivo ya existe')
    # else:
    #   with open(file_path, 'w', encoding='utf-8') as file:
    #     file.write(SCRIPT)



if __name__ == "__main__":
  main()






# # Especifica la ruta del archivo .bat que deseas crear
# archivo_bat = 'mi_script.bat'

# # Escribe el contenido en el archivo
# with open(archivo_bat, 'w') as archivo:
#     archivo.write(script_content)

# print(f'Se ha creado el archivo {archivo_bat}')
