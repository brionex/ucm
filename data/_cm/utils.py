import os
import shutil
from pathlib import Path
import json
from Texts import Text
from modules import env


# Ruta del archivo cm.json
PATH_JSON = Path(env.DATA_DIR) / '_cm' / 'cm.json'


def load_json():
    try:
        with open(PATH_JSON, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading JSON from {PATH_JSON}: {e}") from e


def save_json(data):
    try:
        with open(PATH_JSON, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading JSON from {PATH_JSON}: {e}") from e


def command_exists(name):
    json_data = load_json()

    in_system = shutil.which(name) is not None
    in_reserved = name in json_data['cmds_reserved']
    in_json = name in json_data['cmds']

    return in_system or in_reserved or in_json


def create_command_files(name, template):
    bat_file = Path(env.BIN_DIR) / f'{name}.cmd'
    py_file = Path(env.DATA_DIR) / name / f'{name}.py'

    os.makedirs(Path(env.DATA_DIR) / name, exist_ok=True)
    with open(bat_file, 'w', encoding="utf-8") as cmd_file:
        cmd_file.write(template)
    with open(py_file, 'w', encoding="utf-8") as py_file:
        py_file.write(Text.py_content.format(name))


def remove_command(name, json_data):
    bat_file = Path(env.BIN_DIR) / f'{name}.cmd'
    data_folder = Path(env.DATA_DIR) / name

    os.remove(bat_file)
    shutil.rmtree(data_folder)
    del json_data['cmds'][name]
    save_json(json_data)


def modify_command(command, name, description, json_data):
    if description:
        json_data['cmds'][command] = description

    if name:
        bat_file = Path(env.BIN_DIR) / f'{command}.cmd'
        py_folder = Path(env.DATA_DIR) / command
        py_file = Path(env.DATA_DIR) / command / f'{command}.py'

        new_bat_file = Path(env.BIN_DIR) / f'{name}.cmd'
        new_py_folder = Path(env.DATA_DIR) / name
        new_py_file = Path(env.DATA_DIR) / command / f'{name}.py'

        template = json_data['cmd_template'].format(name)
        with open(bat_file, 'w', encoding='utf-8') as file:
            file.write(template)

        bat_file.rename(new_bat_file)
        py_file.rename(new_py_file)
        py_folder.rename(new_py_folder)

        json_data['cmds'][name] = json_data['cmds'].pop(command)

    save_json(json_data)
