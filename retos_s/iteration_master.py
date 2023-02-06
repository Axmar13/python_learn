'''
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 '''

import random

def one():
    for i in range(1, 101):
        print(i)

def two():
    [print(i) for i in range(1, 101)]

def three():
    i = 1
    while i < 101:
        print(i)
        i += 1

def four():
    """
    Generando números random e imprimiendo el último valor solo si es el número siguiente.
    """
    last_number = 1

    while last_number < 101:
        random_number = random.randint(1, 101)

        if random_number == last_number + 1:
            print(last_number)
            last_number = random_number

def five():
    """
    Utiliza una variable del tipo set, la cual se le va añadiendo un número al azar del 1 al 100. Se ordena e imprime
    cada valor
    """
    series = set()

    while len(series) < 100:
        series.add(random.randint(1, 100))

    series = sorted(series)
    for i in series:
        print(i)

def six():
    """
    Similar a five pero utiliza una lista en vez de un set.
    """
    numbers = []

    while len(numbers) < 100:
        gen_random = random.randint(1, 100)

        if gen_random not in numbers:
            numbers.append(gen_random)

    numbers = sorted(numbers)
    [print(f"{item}") for item in numbers]

one()
two()
three()
four()
five()
six()