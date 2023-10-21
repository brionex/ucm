@echo off

:: Nombre de la carpeta y archivos
set folder=%~1
set html_file="%folder%\index.html"
set css_file="%folder%\styles.css"
set js_file="%folder%\script.js"

:: Comprobar si se proporciona un nombre de carpeta como argumento
if "%~1"=="" (
  echo Se require especificar el nombre del proyecto.
  goto end  
)

:: Comprobar si la carpeta ya existe
if exist "%folder%" (
  echo La carpeta "%folder%" ya existe.
  echo.
  goto end
) else (
  mkdir "%folder%"
)


:: Crear el archivo HTML y agregar la estructura base
(
  echo ^<!DOCTYPE html^>
  echo ^<html lang="es"^>
  echo ^<head^>
  echo   ^<meta charset="UTF-8"^>
  echo   ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
  echo   ^<title^>base web^</title^>
  echo   ^<link rel="stylesheet" href="./styles.css"^>
  echo   ^<script defer src="./script.js"^>^</script^>
  echo ^</head^>
  echo ^<body^>
  echo.
  echo.   
  echo.
  echo ^</body^>
  echo ^</html^>
) > %html_file%


:: Crear el archivo CSS
(
  echo * {
  echo   margin: 0;
  echo   padding: 0;
  echo   box-sizing: border-box;
  echo }
  echo.
  echo body {
  echo   font-family: sans-serif;
  echo }
  echo.
) > %css_file%

:: Crear el archivo JavaScript
echo. > %js_file%


echo Se creo la carpeta %folder% con tres archivos:
echo - index.html
echo - styles.css
echo - script.js
echo.
:end