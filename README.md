# Command Manager (cm)

Una herramienta para gestionar comandos personalizados creados por el usuario.

## Comandos Disponibles
- **add**: Crea los archivos para un nuevo comando.
- **check**: Verifica si un comando ya existe en el sistema.
- **list**: Lista todos los comandos creados por el usuario.
- **modify**: Modifica el nombre o la descripción de un comando existente.
- **open**: Abre el directorio de un comando en Visual Studio Code.
- **remove**: Elimina un comando creado por el usuario.

## Uso
```bash
❯ cm
Usage: ❯ cm [OPTIONS] COMMAND [ARGS]...

  Gestiona los comandos creados por el usuario
```

## Opciones Generales
- `--help`  Muestra este mensaje de ayuda y termina la ejecución.

## Descripción de Comandos

### `add`
Crea los archivos para un nuevo comando.

**Uso:**
```bash
❯ cm add NAME [OPTIONS]
```
**Opciones:**
- `-d, --description`  Proporciona una descripción opcional para el comando.

### `check`
Verifica si un comando ya existe en el sistema.

**Uso:**
```bash
❯ cm check NAME
```
Este comando toma el nombre del comando como argumento y verifica si ya está registrado en el sistema.

### `list`
Lista todos los comandos creados por el usuario.

**Uso:**
```bash
❯ cm list
```
Este comando muestra una lista de todos los comandos personalizados, junto con sus descripciones.

### `modify`
Modifica el nombre o la descripción de un comando existente.

**Uso:**
```bash
❯ cm modify COMMAND [OPTIONS]
```
**Opciones:**
- `-n, --name`        Nuevo nombre para el comando.
- `-d, --description` Nueva descripción para el comando.

### `open`
Abre el directorio de un comando en Visual Studio Code.

**Uso:**
```bash
❯ cm open COMMAND
```
Este comando abre el directorio donde se encuentra el comando especificado en Visual Studio Code.

### `remove`
Elimina un comando creado por el usuario.

**Uso:**
```bash
❯ cm remove COMMAND
```
Este comando elimina el comando especificado del sistema, previa confirmación del usuario.