num1, num2 = 0, 1
while num2 < 1598:
    print(num1, num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2
print("")
num1, num2 = 0, 1
while num2 < 1598:
    print(num1, num2, sep=", ")
    num1 = num1 + num2
    num2 = num1 + num2
print("\nFin.")