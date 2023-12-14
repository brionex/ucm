@echo off

set "archivo=C:\Users\leonel\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"

if "%1" == "-show" (
    type "%archivo%"
    exit /b
)

if exist "%archivo%" (
    del "%archivo%"
    echo El archivo fue eliminado exitosamente.
) else (
    echo El archivo no existe.
)
