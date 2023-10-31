@echo off
set "filename=eslintrc.json"
set "origin=L:\programming\Scripts\programs\eslintconfig\%filename%"

:: Comprobar si se proporciona el argumento "-d"
if "%~1" == "-d" goto DeleteFile
if not "%~1" == "" (
  echo Subcomando no valido.
  goto end
)

:: Verificar si el archivo ya existe antes de crearlo
if exist "%filename%" goto FileExists
if exist "%origin%" goto CopyFile

:DeleteFile
if exist "%filename%" (
  del "%filename%" 2>nul
  if not exist "%filename%" (
    echo El archivo %filename% ha sido eliminado.
  ) else (
    echo Error al eliminar el archivo %filename%.
  )
) else (
  echo El archivo %filename% no existe en la ruta actual.
)
goto end

:FileExists
echo El archivo %filename% ya existe en la ruta actual:
echo %CD%\%filename%
goto end

:CopyFile
copy "%origin%" "%CD%" > nul
if exist "%filename%" (
  echo Archivo %filename% generado en:
  echo %CD%\%filename%
) else (
  echo Error al generar el archivo %filename%.
)
goto end

:end
echo.
