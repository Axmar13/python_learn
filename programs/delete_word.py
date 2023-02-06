frase = input("Introduce una frase: ")
palabra = input("Introduce la palabra que deseas eliminar: ")
substring = ""
indice = frase.find(palabra)
substring = frase[: indice] + frase[indice + len(palabra) + 1 :]
print(f"Cadena resultante: {substring}")
print("Fin.")