cantf = int(input("¿Cuántas filas tendrá la matriz?: "))
cantc = int(input("¿Cuántas columnas tendrá la matriz?: "))
matriz = []
for i in range(cantf):
    fila = []
    for j in range(cantc):
        fila.append(int(input(f"Introduce un elemento a la fila {i}: ")))
    matriz.append(fila)
for i in matriz:
    print(i)