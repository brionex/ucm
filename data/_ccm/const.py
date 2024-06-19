import dataclasses

@dataclasses.dataclass
class CONST:
    ccm = 'Gestiona los comandos creados por el usuario'
    ls = 'Lista todos los comandos creados'
    add = 'Crea los archivos para un nuevo comando'
    remove = 'Elimina un comando creado por el usuario'
    modify = 'Modifica el nombre o la descripción de un comando'
    add_op = 'Agrega una descripción al comando'
    modify_desc = 'Modifica la descripción de un comando'
    modify_name = 'Modifica el nombre de un comando'

    cmd_exist = '\n!Ya existe un comando con ese nombre\n'
    invalid_name = '\n!Nombre de comando no válido\n  * Solo letras minúsculas\n  * Longitud mínima 2 caracteres\n'
    py_content = r'print("\n  Ejecución del archivo {0}.py\n")'
    cmd_created = '\nComando "{0}" creado con éxito.\n'
    confirm_remove = 'Confirmar eliminar comando "{0}" (y): '
    cmd_removed = '\n!Comando eliminado con éxito\n'
    remove_cancel = '\nEliminación cancelada\n'
    cmd_remove_invalid = '\n!No puedes eliminar este comando\n'
    cmd_not_exist = '\n!El comando que deseas eliminar no existe\n'
    cmd_files_not_exist = '\n!Los archivos del comando a eliminar no existen\n'
    unspecified_option = '\nNo se modificó, debes especificar una opción\n'
