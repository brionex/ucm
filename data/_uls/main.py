import sys, os

list = {
    'baseweb': 
    'Crea una carpeta base para un proyecto web.',
    
    'cloudflared': 
    'Proporciona una url que apunta a tu servidor local.',
    
    'comprimg': 
    'Comprime imágenes.',
    
    'eslintconfig': 
    'Crea un archivo de configuración de linter.',
    
    'mysql': 
    'Ejecuta una consola de SQL para realizar consultas.',
    
    'uls': 
    'Muestra una lista de comandos personalizados del usuario.',
}

if not len(sys.argv) > 1:
    print('\nUser command list.')
    for item in list: print(f' - {item}')
    print('\nFor more information about a command.\n - uls <command>\n')
else:
    print(f'\nInfo of command - {sys.argv[1]}\n')
    print(f' - {list[sys.argv[1]]}\n')
