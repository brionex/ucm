@echo off

set "base=%~dp0"
set "venv=%base%data\_venv\Scripts\python.exe"
set "file=%base%data\eslintrc\eslintrc.py"

%venv% %file% %base% %CD%




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
