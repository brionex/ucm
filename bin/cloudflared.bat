:: Documentacion

@echo off

set "DIRNAME=%~dp0"

if "%~1" == "" (
  echo  !Debes ingresar una url valida.
  echo.
  goto end
)

"%DIRNAME%data\cloudflared\cloudflared.exe" tunnel --url %~1

:end