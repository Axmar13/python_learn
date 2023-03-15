import re

def validate_password(password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
    # r significa "raw string" para evitar conflictos con caracteres especiales
    # ^ indica el inicio de la cadena
    # (?=.*[a-z]) indica que debe contener al menos una letra minúscula
    # (?=.*[A-Z]) indica que debe contener al menos una letra mayúscula
    # (?=.*\d) indica que debe contener al menos un dígito
    # [a-zA-Z\d]{6,} indica que debe tener al menos 6 caracteres alfanuméricos
    # $ indica el final de la cadena
    return bool(re.match(regex, password))