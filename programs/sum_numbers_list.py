cantnum = int(input("¿Cuántos números enteros contendrá la lista?: "))
lista = []
for _ in range(cantnum):
    lista.append(int(input("Introduce un número entero: ")))
print(f"Lista: {lista}")
print(f"La suma total de los elementos es: {sum(lista)}")