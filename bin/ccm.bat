@echo off
set "dirname=%~dp0.."
set "venvpy=%dirname%\.venv\Scripts\python.exe"
set PYTHONPATH="%dirname%\modules";%PYTHONPATH%
%venvpy% "%dirname%\data\_ccm\ccm.py" %*
