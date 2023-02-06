'''
 * Enunciado: Crea un programa se encargue de transformar un número binario
 * a decimal sin utilizar funciones propias del lenguaje que 
 * lo hagan directamente.
'''

binary = "10011011"
decimal = 0
for i, char in enumerate(reversed(binary)):
    if char == "1":
        decimal += 2 ** i
print(decimal)