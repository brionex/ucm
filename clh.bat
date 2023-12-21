@REM Documentacion.

:: Borra el historial de comandos ingresados en la consola.
:: Es necesario reiniciar la consola para notar el cambio.
:: ( clh -show ) - Muestra todo el historial de comandos.


@echo off

set "archivo=%AppData%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"

if "%~1" == "-show" (
    echo.
    type "%archivo%"
    echo.
    exit /b
)

if exist "%archivo%" (
    del "%archivo%"
    echo.
    echo * El archivo fue eliminado exitosamente.
    echo.
) else (
    echo.
    echo * El archivo no existe.
    echo.
)
