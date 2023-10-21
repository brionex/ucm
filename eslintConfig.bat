@echo off
set "outputPath=%CD%\eslintrc.json"
echo.

rem Verificar si el archivo ya existe antes de crearlo
if not exist "%outputPath%" (
  (
  echo {
  echo   "extends": ["standard", "standard-jsx"],
  echo   "rules": {
  echo     "space-before-function-paren": "off",
  echo     "no-trailing-spaces": ["error", { "skipBlankLines": true }],
  echo     "no-multiple-empty-lines": ["error", { "max": 3, "maxEOF": 1 }],
  echo     "comma-dangle": ["error", "only-multiline"]
  echo   }
  echo }
  ) > "%outputPath%"
  echo Archivo eslintrc.json generado en: %outputPath%
) else (
  echo El archivo eslintrc.json ya existe en: %outputPath%
)

echo.