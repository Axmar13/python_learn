'''
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
 * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 '''

def is_palindrome(text: str):
    out_text = text.lower()
    for char in out_text:
        if char == ' ' or char == '.' or char == ',' or char == ':' or char == ';' or char == '!' or char == '¡' or char == '?' or char == '¿':
            out_text = out_text.replace(char, "")
    return out_text == out_text[::-1]

phrase = input("Ingrese una frase: ")
print(f"¿Es la frase un palíndromo?: {is_palindrome(phrase)}")