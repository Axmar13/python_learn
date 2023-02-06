'''
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
'''

def print_words_in_frame(phrase: str):
    max_lenght = 0
    for word in phrase.split(" "):
        if len(word) > max_lenght:
            max_lenght = len(word)
    print((max_lenght + 2) * "*")
    for word in phrase.split(" "):
        print(f"*{word}" + (max_lenght - len(word)) * " " + "*")
    print((max_lenght + 2) * "*")
    print("\n")

print_words_in_frame("Ley de la sorpresa")
print_words_in_frame("Kingdom Hearts")
print_words_in_frame("Nada es verdad, todo está permitido")
print_words_in_frame("What doesn't kill me... better start running!")