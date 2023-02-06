'''
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
'''

def next_leap_years(year: int):
    i = 0
    while i < 30:
        year += 1
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 
            print(year)
            i += 1

next_leap_years(1945)