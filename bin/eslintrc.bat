:: Documentacion

@echo off

set "base=%~dp0"
set "venv=%base%data\_venv\Scripts\python.exe"
set "file=%base%data\eslintrc\eslintrc.py"

%venv% %file% %base% %CD%