@echo off

if "%~1" == "" (
  echo !Debes ingresar una url valida.
  echo.
  goto end
)

"L:\programming\Scripts\programs\cloudflared\cloudflared.exe" tunnel --url %~1

:end