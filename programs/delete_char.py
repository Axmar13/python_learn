lista = ["A", "B", "b", "c", "E", "E", "f"]
print(f"Lista original: {lista}")
char = input("Introduce el elemento que desead eliminar: ")
for _ in lista:
    if char.lower() in lista:
        lista.remove(char.lower())
    elif char.upper() in lista:
        lista.remove(char.upper())
print(f"Elemento eliminado: {lista}")