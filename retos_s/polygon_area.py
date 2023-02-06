'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def poly_area(polygon, b = 0, h = 0):
    if polygon == 1:
        a = (b * h) / 2
    else:
        a = b * h        
    return a

poly, b, h = 0, 0, 0

while poly != 1 and poly != 2 and poly != 3: 
    poly = int(input("¿El área de que polígono desea calcular?\n\t1) Triángulo\n\t2) Cuadrado\n\t3) Rectángulo\nOpción (1-3): "))
    if poly != 1 and poly != 2 and poly != 3:
        print("Elige una opción válida (1-3).\n")

if poly == 1:
    while b <= 0: 
        b = int(input("Ingrese la base del triángulo: "))
        if b < 0:
            print("La base no puede ser menor o igual a 0.\n")
    while h <= 0: 
        h = int(input("Ingrese la altura del triángulo: "))
        if h < 0:
            print("La altura no puede ser menor o igual a 0.\n")
    print(f"El área del triángulo es {poly_area(poly, b, h)}")

if poly == 2:
    while b <= 0: 
        b = int(input("Ingrese un lado del cuadrado: "))
        if b < 0:
            print("El lado no puede ser menor o igual a 0.\n")
    h = b
    print(f"El área del cuadrado es {poly_area(poly, b, h)}")

if poly == 3:
    while b <= 0:
        b = int(input("Ingrese la base del rectángulo: "))
        if b < 0:
            print("La base no puede ser menor o igual a 0.\n")
    while h <= 0: 
        h = int(input("Ingrese la altura del rectángulo: "))
        if h < 0:
            print("La altura no puede ser menor o igual a 0.\n")
    print(f"El área del rectángulo es {poly_area(poly, b, h)}")