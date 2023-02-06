'''
 * Enunciado: Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
'''

def calculate_value(V: int = 0, R: int = 0, I: int = 0):
    if V == 0 and R > 0 and I > 0:
        V = R * I
        print("El valor del voltaje es: ", end="")
        return round(V, 2)
    elif R == 0 and V > 0 and I > 0:
        R = V / I
        print("El valor de la resistencia es: ", end="")
        return round(R, 2)
    elif I == 0 and R > 0 and V > 0:
        I = V / R
        print("El valor de la corriente es: ", end="")
        return round(I, 2)
    else:
        return "Invalid values"

print(calculate_value(V=12, R=6))
print(calculate_value(R=22, I=0.6))
print(calculate_value(V=24, I=0.3))