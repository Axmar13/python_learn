'''
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


string = input("Introduce un string para invertirlo: ")
string_invested = ""
for character in string:
    string_invested = character + string_invested
print(f"String invertido: {string_invested}")
'''

def inv_string(string = 0):
    return string[::-1]

print(f"La cadena invertida es: {inv_string(input('Introduce el texto a invertir: '))}")