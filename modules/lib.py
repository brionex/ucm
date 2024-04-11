import re

def validate_alphanumeric(text):
    """
    La expresión regular permite strings que contengan letras (mayúsculas y minúsculas), 
    dígitos del 0 al 9, guiones bajos (_) y guiones (-), pero no permite espacios ni 
    otros caracteres especiales. 
    """
    return bool(
        re.match(r'^[a-zA-Z0-9_-]+$', text)
    )


def validate_lowercase(text):
    """
    La expresión regular permite solo strings que sean solo letras en minúsculas, 
    sin espacios, símbolos y sin números. 
    """
    return bool(
        re.match(r'^[a-z]+$', text)
    )
