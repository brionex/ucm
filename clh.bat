@REM Documentacion.

:: Borra el historial de comandos ingresados en la consola.
:: Es necesario reiniciar la consola para notar el cambio.
:: ( clh -show ) - Muestra todo el historial de comandos.


@echo off

set "historyFile=%AppData%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"

if "%~1" == "-show" (
    echo.
    type "%historyFile%"
    echo.
    exit /b
)

if exist "%historyFile%" (
    del "%historyFile%"
    echo.
    echo * Se ha borrado todo el historial.
    echo.
) else (
    echo.
    echo * No existe historial de la consola.
    echo.
)
