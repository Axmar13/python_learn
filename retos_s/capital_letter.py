'''
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 '''

def title_case(phrase: str):

    list_word = [word[0].upper() + word[1::].lower() for word in phrase.split(" ")]

    return " ".join(list_word)


# Test
print(title_case("hola mundo"))
print(title_case("mOuRedEV bY brais mOUre."))
print(title_case("no a la manzanilla..."))