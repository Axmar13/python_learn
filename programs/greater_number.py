num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 > num2 and num1 > num3:
    print("El número más grande es el ", num1)
elif num2 > num3:
    print("El número más grande es el ", num2)
else:
    print("El número más grande es el ", num3)
print("Fin.")