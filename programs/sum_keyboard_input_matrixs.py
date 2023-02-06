cantm, cantf, cantc = 0, 0, 0
while cantm < 2:
    cantm = int(input("\n¿Cuántas matrices vamos a sumar?: "))
    if cantm < 2:
        print("Se necesitan dos o más matrices para realizar la suma.")
while cantf < 1:
    cantf = int(input("\n¿Cuántas filas tendrán las matrices?: "))
    if cantf < 1:
        print("La matriz debe tener al menos una fila.")
while cantc < 1:
    cantc = int(input("\n¿Cuántas columnas tendrán las matrices?: "))
    if cantc < 1:
        print("La matriz debe tener al menos una columna.")
#Pedido de matrices
matrizm = []
for i in range(cantm):
    matriz = []
    for j in range(cantf):
        fila = []
        for k in range(cantc):
            fila.append(int(
                input(f"Introduce un elemento para la matriz {i+1} fila {j} columna {k}: ")))
        matriz.append(fila)
    matrizm.append(matriz)
#Suma de matrices
matrizsuma = []
for i in range(cantf):
    fila = []
    for j in range(cantc):
        suma = 0
        for posmatriz in range(len(matrizm)):
            suma += matrizm[posmatriz][i][j]
        fila.append(suma)
    matrizsuma.append(fila)
matrizm.append(matrizsuma)
#Impresión de matrices
for fila in range(cantf):
    for matrizactual in range(len(matrizm)):
        if fila != 1:
            print (f"{matrizm[matrizactual][fila]}", end="   ")
        else:
            if matrizactual < len(matrizm) - 2:
                print (f"{matrizm[matrizactual][fila]}", end=" + ")
            elif matrizactual < len(matrizm) - 1:
                print (f"{matrizm[matrizactual][fila]}", end=" = ")
            else:
                print (f"{matrizm[matrizactual][fila]}", end="   ")
    print()