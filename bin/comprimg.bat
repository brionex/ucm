:: Documentacion

@echo off

@rem comprimg
@rem comprimg nombre
@rem comprimg -s 200x200
@rem comprimg nombre -s 200x200
@rem comprimg -s 200x200 nombre

setlocal enabledelayedexpansion

set "DIRNAME=%~dp0"
set command=python "L:\programming\Scripts\programs-scripts\image-compressor.py" %CD%
set p1=%~1
set p2=%~2
set p3=%~3

@rem comprimg
if "%p1%" == "" (
  echo 1
  %command%
  goto end
)

@rem comprimg nombre
if not "%p1%" == "" if "%p2%" == "" (
  echo 2
  %command% %p1%
  goto end
)

@rem comprimg -s 200x200
if "%p1%" == "-s" if not "%p2%" == "" (
  echo 3
  %command% "s:%p2%"
  goto end
)

@rem comprimg nombre -s 200x200
if not "%p1%" == "" if "%p2%" == "-s" if not "%p3%" == "" (
  echo 4
  %command% %p1% "s:%p3%"
  goto end
)

@rem comprimg -s 200x200 nombre
if "%p1%" == "-s" if not "%p2%" == "" if not "%p3%" == "" (
  echo 5
  %command% "s:%p2%" %p3%
  goto end
)

:end
endlocal