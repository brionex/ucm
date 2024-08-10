import dataclasses


@dataclasses.dataclass
class Text:
    ls_title = '\nComandos del Usuario\n'

    check_exist = '\nEl comando "{0}" sí existe en el sistema\n'
    check_not_exist = '\nEl comando "{0}" no existe en el sistema\n'

    add_option = 'Agrega una descripción al comando'
    add_created = '\n!Comando "{0}" creado con éxito\n'

    remove_confirm = '\nConfirmar eliminación del comando "{0}" (y): '
    remove_removed = '\nComando eliminado con éxito\n'
    remove_cancel = '\nEliminación cancelada\n'
    remove_invalid = '\n!No puedes eliminar este comando\n'
    remove_not_exist = '\n!El comando que deseas eliminar no existe\n'

    modify_name = 'Modifica el nombre de un comando'
    modify_desc = 'Modifica la descripción de un comando'
    modify_invalid = '\n!No puedes modificar este comando\n'
    modify_modified = '\nComando modificado con éxito\n'
    modify_not_option = '\n!Debes especificar una opción para modificar\n'
    modify_not_exist = '\n!El comando que deseas modificar no existe\n'

    open_invalid = '\n!No puedes editar los archivos de este comando\n'
    open_not_exist = '\n!No existe el comando que deseas abrir\n'
    open_error = "\nError al intentar abrir la carpeta en VS Code: {0}\n"
    open_not_vscode = "\nEl comando 'code' no se encontró\n"
    open_success = '\nDirectorio de comando "{0}" se abrió en vscode\n'

    cmd_exist = '\n!Ya existe un comando con ese nombre en el sistema\n'
    invalid_name = '\n!Nombre de comando no válido\n  * Solo letras minúsculas\n  * Longitud mínima: 2 caracteres\n'
    py_content = 'print("Ejecución del archivo {0}.py")\n'
