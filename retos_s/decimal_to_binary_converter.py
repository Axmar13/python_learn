'''
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def dec_bin_conv(num: int):
    reminder, bin = 0, ""
    while num != 1:
        reminder = num % 2
        bin += str(reminder)
        num = num // 2
    bin += str(reminder)
    bin = bin[::-1]
    print(bin)

dec_bin_conv(int(input("Ingrese el número que desea convertir: ")))