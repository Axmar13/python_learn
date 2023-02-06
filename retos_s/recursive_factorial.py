'''
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
'''

def factorial(num):
    print("Valor inicial ->", num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->", num)
    return num

print(factorial(5))