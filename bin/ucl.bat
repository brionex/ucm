@echo off
set "dirname=%~dp0"
set "venvpy=%dirname%..\.venv\Scripts\python.exe"
%venvpy% "%dirname%..\data\_ucl\ucl.py" %*