'''
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información 
 * al respecto.
'''

def is_armstrong(number: int):
    result = 0
    string_num = str(number)
    for num in string_num:
        result += int(num) ** len(string_num)

    if result == number:
        return True
    else:
        return False

num = int(input("Ingrese el número: "))
print(is_armstrong(num))