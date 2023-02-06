'''
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
'''

def ms_convert(days: int, hours: int, mins: int, secs: int) -> int:
    return (((((days * 24) * 60) * 60) * 1000) + (((hours * 60) * 60) * 1000) + ((mins * 60) + secs) * 1000)

print(f"Milisegundos: {ms_convert(13, 13, 13, 13)}")
print(f"Milisegundos: {ms_convert(13, 0, 0, 0)}")