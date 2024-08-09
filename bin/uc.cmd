@echo off
setlocal
set "dirname=%~dp0.."
set "venvpy=%dirname%\.venv\Scripts\python.exe"
set PYTHONPATH=%dirname%;%PYTHONPATH%
"%venvpy%" "%dirname%\data\_uc\uc.py" %*
IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
endlocal

