num = int(input("¿Qué tabla de multiplicar quieres ver?: "))
print(f"La tabla del {num} es:")
for i in range(0, 11):
    print(f"{num} x {i} = {num * i}")
print("\nFin.")