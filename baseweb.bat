:: 

@echo off
setlocal enabledelayedexpansion

set "DIRNAME=%~dp0"
set "template=%DIRNAME%data\baseweb\template"


:: Verifica si debe crear carpeta por defecto o por argumneto.
if not "%~1" == "" (
  set "folder=%~1"
) else (
  set "folder=baseweb"
)

:: Crea la carpe si no existe.
if not exist "%folder%" (
  mkdir "%folder%" 2>nul
  if exist "%folder%" (
    echo Proyecto generado en la ruta actual:
    echo '%CD%\%folder%'
  ) else (
    echo Error al crear el proyecto.
    goto end
  )
) else (
  echo Ya existe un proyecto llamado '%folder%' en la ruta actual.
  goto end
)

:: Copia la plantilla al directorio creado.
xcopy %template% %folder% /e > nul

:end
endlocal
echo.
