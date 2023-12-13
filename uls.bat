@echo off

set "base=%~dp0"
set "pyenv=%base%\data\_pyenv\Scripts\python.exe"
set "ulsfile=%base%\data\_uls\main.py"

:: echo %base%
:: echo %pyenv%
:: echo %ulsfile%

%pyenv% %ulsfile% %~1
