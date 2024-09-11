class Text:
    NO_RELEASE_FOLDER = "\nNo se encontró la carpeta 'release'.\n"
    PYINSTALLER_MISSING = "\nNo se encontró el script de PyInstaller.\n"
    BUILD_START = "\nCompilación iniciada..."
    PACKAGING_APP = "Empaquetando aplicación..."
    PACKAGING_DONE = "Aplicación empaquetada"
    COLLECT_ADDITIONAL = "Recopilando archivos adicionales"
    BUILD_END = "Compilación finalizada.\n"
    PREVIEW_ERROR = "Error al ejecutar el archivo 'ucm.exe'."
    NO_APP_EXE = "No se encontró el archivo 'ucm.exe'."

    # Mensajes del entorno virtual
    venv_name = ".venv"
    venv_creating = "\nCreando entorno virtual..."
    venv_created = "Entorno virtual creado correctamente."
    venv_exists = "El entorno virtual ya existe.\n"
    venv_failed = "Creación del entorno virtual fallida."
    env_ready = "Entorno de desarrollo listo.\n"

    # Mensajes de instalación de dependencias
    deps_installing = "Instalando dependencias..."
    deps_installed = "\nDependencias instaladas correctamente.\n"
    no_requirements = "Archivo 'requirements.txt' no encontrado.\n"

    # Mensajes de compilación de la aplicación
    app_compiled = "\nAplicación 'ucm' compilada correctamente.\n"
    app_installed = "\nAplicación 'ucm' instalada correctamente.\n"

    # Mensajes del uso de run.py
    usage = "\nUso: python run.py [comando] [args...]\n"
    cmd_unknown = "\nComando no reconocido: {0}\n"

    # Mensajes que usan los comandos de run.py
    build_zip_start = "Comprimiendo archivos..."
    build_zip_end = "Archivos comprimidos en un zip"

    no_write_perm = "No tienes permisos de escritura en esta carpeta.\n"
    cli_ucm_error = "Error al ejecutar el CLI de 'ucm': {0}"
