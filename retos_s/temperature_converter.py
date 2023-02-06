'''
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" 
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 * - ¿Quieres emplear lo aprendido en este reto?
 *   Revisa el reto mensual y crea una App: 
 *   https://retosdeprogramacion.com/mensuales2022
'''


def temp_conversion(temperature: str):
    if "°C" in temperature:
        index = temperature.index("°")
        result = (int(temperature[0:index]) * 9 / 5) + 32
        result = temperature + " equivale a " + str(round(result, 2)) + "°F"
        return result
    if "°F" in temperature:
        index = temperature.index("°")
        result = (int(temperature[0:index]) - 32) * 5 / 9
        result = temperature + " equivale a " + str(round(result, 2)) + "°C"
        return result
        

print(temp_conversion(input(
    "Ingrese el valor a convertir con su respectivo símbolo e identificador de unidad de medida (°C o °F): ")))
