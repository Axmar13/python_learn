print("===========\n\"Conversor\"\n===========")
print("Ingrese 1 para convertir de número a palabra.")
print("Ingrese 2 para convertir de palabra a número.")
opcion = int(input("\n¿Cúal es tu opción deseada?: "))
if opcion == 1:
    print("\nConversor de número a palabra")
    numero = int(input("\n¿Cúal es el número que deseas convertir?: "))
    if numero == 0:
        print("El número es 'Cero'")
    elif numero == 1:
        print("El número es 'Uno'")
    elif numero == 2:
        print("El número es 'Dos'")
    elif numero == 3:
        print("El número es 'Tres'")
    elif numero == 4:
        print("El número es 'Cuatro'")
    elif numero == 5:
        print("El número es 'Cinco'")
    else:
        print("Este programa solo convierte hasta 5")
elif opcion == 2:
    print("\nConversor de palabra a número")
    numerop = input("\n¿Cúal es la palabra que deseas convertir?: ")
    numerop = numerop.lower()
    if numerop == "cero":
        print("El número es '0'")
    elif numerop == "uno":
        print("El número es '1'")
    elif numerop == "dos":
        print("El número es '2'")
    elif numerop == "tres":
        print("El número es '3'")
    elif numerop == "cuatro":
        print("El número es '4'")
    elif numerop == "cinco":
        print("El número es '5'")
    else:
        print("Este programa solo convierte hasta 5")
else:
    print("\nOpción no válida.")
print("\nFin.")