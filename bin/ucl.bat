:: Muestra una lista de los comandos personalizados del usuario.

@echo off

set "base=%~dp0"
set "venv=%base%data\_venv\Scripts\python.exe"
set "file=%base%data\_ucl\ucl.py

%venv% %file% %base% %~1 %~2
