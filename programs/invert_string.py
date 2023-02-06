frase = input("Introduce un string para invertirlo: ")
fraseinv = ""
for character in frase:
    fraseinv = character + fraseinv
print(f"String invertido: {fraseinv}")