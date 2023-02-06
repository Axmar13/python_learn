lista = [1, 2, 3, 4, 5]
print(f"Lista números: {lista}")
sublista = []
sublista.append(lista.pop(0))
sublista.append(lista.pop())
print(f"Lista números: {lista}")
print(f"Lista números eliminados: {sublista}")