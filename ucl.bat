:: Documentaciion del comando - ucl

:: Muestra una lista de los comandos personalizados del usuario.
::: holasadasdas as d asd s  dsa d sa da s
::: sadasdasds ad asd as das d asd 

:: otro sms
::: - 1lista

@echo off

set "base=%~dp0"
set "venv=%base%data\_venv\Scripts\python.exe"
set "file=%base%data\_ucl\ucl.py

%venv% %file% %base% %~1 %~2
