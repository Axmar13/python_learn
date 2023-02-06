nombre = input("¿Cuál es tu nombre?: ")
mat = float(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
qui = float(input(nombre + " ¿Cuál es tu calificación en química?: "))
bio = float(input(nombre + " ¿Cuál es tu calificación en biología?: "))

promedio = (mat + qui + bio) / 3

if promedio >= 6:
    print("Felicidades " + nombre + " \"aprobaste\" con un promedio de: ", round(promedio, 2))
else:
    print("Lamentablemente " + nombre + ", \"reprobaste\" con un promedio de: ", round(promedio, 2))

print("Fin.")