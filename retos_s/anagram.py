'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def anagrama(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    return False

a = input("Palabra 1: ")
b = input("Palabra 2: ")
print()
print(anagrama(a, b))
print("\nFin.")