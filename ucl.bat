:: Documentaciion del comando - uls

@echo off

set "base=%~dp0"
set "pyenv=%base%data\_pyenv\Scripts\python.exe"
set "ulsfile=%base%data\_uls\main.py"
set "command=ucl"



if "%~2" == "" (
  @REM Pasa los argumentos necesarios.
  %pyenv% %ulsfile% %base% %command% %~1

) else (
  @REM Pasa un argumento adicional para mostrar un error de argumentos.
  %pyenv% %ulsfile% %base% %command% %~1 "error"
)



@REM echo %base%
@REM echo %pyenv%
@REM echo %ulsfile%
