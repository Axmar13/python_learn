'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

for j in range(1,101):
    contador = 0
    for i in range(1, j+1):
        if j % i == 0:
            contador += 1
    if contador == 2:
        print(j)