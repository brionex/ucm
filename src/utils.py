import shutil
import json
import os
import re

from messages import Text
import env


class Utils:
    def __init__(self):
        self.json = self.load_json()
        self.json_cmds = self.json['cmds']
        self.json_cmds_reserved = self.json['cmds_reserved']
        self.json_cmd_template = self.json['cmd_template']

        if self.json_cmds:
            self.json_cmd_max = max(len(name) for name in self.json_cmds)

    def load_json(self):
        """Carga el archivo data.json y lo devuelve como un diccionario."""
        try:
            with env.JSON_PATH.open('r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            raise RuntimeError(
                f"Error al cargar el JSON desde {env.JSON_PATH}: {e}"
            ) from e

    def save_json(self):
        """Guarda los cambios del archivo data.json."""
        try:
            with env.JSON_PATH.open('w', encoding='utf-8') as file:
                json.dump(self.json, file, indent=2, ensure_ascii=False)
        except (IOError, OSError) as e:
            raise RuntimeError(
                f"Error al guardar el JSON en {env.JSON_PATH}: {e}"
            ) from e

    def is_valid_name(self, name):
        """
        Verifica si el nombre de un comando es válido:
        longitud mínima 2 y solo letras minúsculas.
        """
        return len(name) >= 2 and bool(re.fullmatch(r'[a-z]+', name))

    def command_exists(self, name):
        """
        Verifica si un comando existe en el sistema o
        en la lista del archivo data.json
        """
        return (
            shutil.which(name) is not None or
            name in self.json_cmds_reserved or
            name in self.json_cmds
        )

    def create_command_files(self, name):
        """Crea los archivos necesarios para un nuevo comando."""
        cmd_file = env.BIN_DIR / f'{name}.cmd'
        py_file = env.DATA_DIR / name / f'{name}.py'

        env.BIN_DIR.mkdir(parents=True, exist_ok=True)
        (env.DATA_DIR / name).mkdir(parents=True, exist_ok=True)

        with cmd_file.open('w', encoding='utf-8') as file:
            file.write(self.json_cmd_template.format(env.VENV_PY, name))

        with py_file.open('w', encoding='utf-8') as file:
            file.write(Text.py_content.format(name))

    def remove_command(self, name):
        """
        Elimina un comando creado por el usuario junto a 
        los archivos y directorios asociados.
        """
        cmd_file = env.BIN_DIR / f'{name}.cmd'
        data_folder = env.DATA_DIR / name

        if cmd_file.exists():
            cmd_file.unlink()

        if data_folder.exists():
            shutil.rmtree(data_folder)

        self.json_cmds.pop(name, None)
        self.save_json()

    def modify_command(self, command, name, description):
        """Modifica el nombre o la descripción de un comando existente."""
        if description:
            self.json_cmds[command] = description

        if name:
            cmd_file = env.BIN_DIR / f'{command}.cmd'
            py_folder = env.DATA_DIR / command
            py_file = py_folder / f'{command}.py'

            new_cmd_file = env.BIN_DIR / f'{name}.cmd'
            new_py_folder = env.DATA_DIR / name
            new_py_file = py_folder / f'{name}.py'

            if cmd_file.exists():
                cmd_file.write_text(
                    self.json_cmd_template.format(env.VENV_PY, name),
                    encoding='utf-8'
                )
                cmd_file.rename(new_cmd_file)

            if py_file.exists():
                py_file.rename(new_py_file)
                py_folder.rename(new_py_folder)

            self.json_cmds[name] = self.json_cmds.pop(command)
        self.save_json()
