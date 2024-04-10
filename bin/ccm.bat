:: Administra los comandos creados por el usuario.

@echo off
set "dirname=%~dp0"
set "venvpy=%dirname%..\.venv\Scripts\python.exe"
set PYTHONPATH=%dirname%..\modules;%PYTHONPATH%
%venvpy% "%dirname%..\ccm\ccm.py" %*