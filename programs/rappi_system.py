print("***************************************\n* Sistema de control vacacional Rappi *\n***************************************\n")
nombre = input("Nombre del empleado: ")
clave = int(input("Clave del empleado: "))
if clave == 1:
    antig = int(input("Antiguedad del empleado: "))
    if antig == 1 and antig < 2:
        print("El empleado " + nombre + " tiene 6 días de vacaciones.")
    elif antig >= 2 and antig <= 6:
        print("El empleado " + nombre + " tiene 14 días de vacaciones.")
    elif antig >= 7:
        print("El empleado " + nombre + " tiene 20 días de vacaciones.")
    else:
        print("El empleado " + nombre + " no tiene derecho a vacaciones.")
elif clave == 2:
    antig = int(input("Antiguedad del empleado: "))
    if antig == 1 and antig < 2:
        print("El empleado " + nombre + " tiene 7 días de vacaciones.")
    elif antig >= 2 and antig <= 6:
        print("El empleado " + nombre + " tiene 15 días de vacaciones.")
    elif antig >= 7:
        print("El empleado " + nombre + " tiene 22 días de vacaciones.")
    else:
        print("El empleado " + nombre + " no tiene derecho a vacaciones.")
elif clave == 3:
    antig = int(input("Antiguedad del empleado: "))
    if antig == 1 and antig < 2:
        print("El empleado " + nombre + " tiene 10 días de vacaciones.")
    elif antig >= 2 and antig <= 6:
        print("El empleado " + nombre + " tiene 20 días de vacaciones.")
    elif antig >= 7:
        print("El empleado " + nombre + " tiene 30 días de vacaciones.")
    else:
        print("El empleado " + nombre + " no tiene derecho a vacaciones.")
else:
    print("La clave no existe.")
print("Fin.")