import json
import os
from pathlib import Path

# Definición de la ruta del archivo de comandos
DOC_FILE = Path(__file__).resolve().parent / 'uc.json'


def cmd_exists(name):
    """
    Verifica si un comando con el nombre proporcionado existe en el PATH.
    """
    paths = os.getenv('PATH', '').split(os.pathsep)

    for path in paths:
        if os.path.isdir(path):
            for filename in os.listdir(path):
                cmd_name, extension = os.path.splitext(filename.lower())
                if extension in ['.exe', '.bat', '.cmd'] and cmd_name == name.lower():
                    return True

    return False


def load_cmds_doc():
    """
    Carga y devuelve el contenido de cmds.json como un diccionario.
    """
    with open(DOC_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


def add_cmd_doc(info):
    """
    Agrega un nuevo comando a cmds.json.
    """
    cmd_list = load_cmds_doc()
    cmd_list.append(info)
    save_cmds_doc(cmd_list)


def save_cmds_doc(cmd_list):
    """
    Guarda la lista de comandos en cmds.json.
    """
    with open(DOC_FILE, 'w', encoding='utf-8') as file:
        json.dump(cmd_list, file, indent=2, ensure_ascii=False)


def get_cmds_list_doc():
    """
    Devuelve una lista con los nombres de los comandos desde cmds.json.
    """
    return [cmd['name'] for cmd in load_cmds_doc()]


def remove_cmd_doc(name):
    """
    Elimina un comando por nombre de cmds.json.
    """
    cmd_list = load_cmds_doc()
    cmd_list = [cmd for cmd in cmd_list if cmd['name'] != name]
    save_cmds_doc(cmd_list)
