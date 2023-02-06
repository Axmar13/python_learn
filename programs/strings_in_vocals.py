frase = input("Introduce una frase: ")
letra = input("¿Con qué letra deseas terminar el bucle?: ")
for i in frase:
    if i.lower() == letra.lower():
        break
    elif i.lower() == "a":
        continue
    elif i.lower() == "e":
        continue
    elif i.lower() == "i":
        continue
    elif i.lower() == "o":
        continue
    elif i.lower() == "u":
        continue
    print(i, end="")