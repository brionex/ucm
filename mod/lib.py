import re

# Valida si un string es valido para un nombre de carpeta.
def validate_folder_name(name):
    pattern = r'^[a-zA-Z0-9_-]+$'
    return re.match(pattern, name) is not None


def saludar():
    print('hola desde los módulos')
