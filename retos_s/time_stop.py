'''
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
'''

import time

def sum_with_pause(num1: int, num2: int, pause_time: int) -> int:
    result = 0
    time.sleep(pause_time)  
    result = num1 + num2
    return result


print(sum_with_pause(13, 13, 13))
print(sum_with_pause(13, 3, 4))
print(sum_with_pause(3, 3, 6))