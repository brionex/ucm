@echo off

set base=%CD%
set pyenv=%CD%\data\_pyenv\Scripts\python.exe
set ulsfile=%CD%\data\_uls\main.py

:: echo %base%
:: echo %pyenv%
:: echo %ulsfile%

%pyenv% %ulsfile%
