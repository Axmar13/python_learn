'''
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que 
 *   lo resuelvan directamente.
'''
'''
def greatest_common_factor(num1: int, num2: int) -> int:
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    if len(factors1) <= len(factors2):
        common_numbers = [n for n in factors1 if n in factors2]
    else:
        common_numbers = [n for n in factors2 if n in factors1]
    return common_numbers[-1]


def least_common_multiple(num1: int, num2: int) -> int:
    prime_numbers = [i for i in range(2, 101) if (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5) and (i % 7 != 0 or i == 7)]
    prime_factors1, prime_factors2, prime_factors_both = [], [], []
    for i in prime_numbers:
        if num1 % i == 0:
            while num1 % i == 0:
                num1 = num1 // i
                prime_factors1.append(i)
        if num2 % i == 0:
            while num2 % i == 0:
                num2 = num2 // i
                prime_factors2.append(i)
    for i in prime_factors1:
        if i not in prime_factors_both:
            prime_factors_both.append(i)
    for i in prime_factors2:
        if i not in prime_factors_both:
            prime_factors_both.append(i)
    print(prime_factors_both)


#print(f"El máximo común divisor de 8 y 12 es: {greatest_common_factor(8, 12)}")
print(f"El mínimo común múltiplo de 8 y 12 es: {least_common_multiple(8, 12)}")
#print(f"El máximo común divisor de 65 y 39 es: {greatest_common_factor(65, 39)}")
print(f"El mínimo común múltiplo de 65 y 39 es: {least_common_multiple(65, 39)}")
'''

# Solución de Oscar
 
def mcd(num1: int, num2: int):
    """
    Se realiza el cálculo del mcd se realiza mediante el algoritmo de Euclides.
    """
    # Se debe determinar el número mayor para asignar a las variables a y b
    if num1 > num2:
        a = num1
        b = num2

    else:
        a = num2
        b = num1

    # Mientras b sea distinto de cero se realiza la operación
    while b:
        mcd = b
        b = a % b
        a = mcd

    # Imprime el valor del mcd
    print(f"El M.C.D de {num1} y {num2} es {mcd}")

    return mcd


def mcm(num1: int, num2: int):
    # Calcula el mcm a partir del mcd y lo imprime
    print(f"El M.C.M de {num1} y {num2} es {(num1*num2) // mcd(num1, num2)}")


# Tests
mcm(10, 5)
mcm(8, 7)
mcm(1, 2)
mcm(21, 17)