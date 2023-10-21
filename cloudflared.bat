@echo off
setlocal
set ARG=%1
"L:\programming\Scripts\cloudflared\cloudflared.exe" tunnel --url %ARG%
endlocal