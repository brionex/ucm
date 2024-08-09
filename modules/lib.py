import re

def validate_alphanumeric(text):
    # Verifica si el texto contiene solo letras, dígitos, guiones bajos o guiones.
    if not isinstance(text, str):
        return False
    return bool(re.fullmatch(r'[a-zA-Z0-9_-]+', text))

def validate_lowercase(text):
    # Verifica si el texto contiene solo letras minúsculas.
    if not isinstance(text, str):
        return False
    return bool(re.fullmatch(r'[a-z]+', text))
