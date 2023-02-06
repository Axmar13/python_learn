q1, q2, q3 = 0, 0, 0
gryffindor, ravenclaw, hufflepuff, slytherin = 0, 0, 0, 0
while q1 != 1 and q1 != 2:
    q1 = int(input("Q1) Cuál te gusta más?\n\t1) Amanecer\n\t2) Anochecer\nOpción (1~2): "))
    if q1 != 1 and q1 != 2:
        print("Elige una opción correcta.\n")

while q2 != 1 and q2 != 2 and q2 != 3 and q2 != 4:
    q2 = int(input("Q2) Cuando muera, quiero que la gente me recuerde como alguien:\n\t1) Bueno\n\t2) Genial\n\t3) Inteligente\n\t4) Valiente\nOpción (1~4): "))
    if q2 != 1 and q2 != 2 and q2 != 3 and q2 != 4:
        print("Elige una opción correcta.\n")

while q3 != 1 and q3 != 2 and q3 != 3 and q3 != 4:
    q3 = int(input("Q3) Qué instrumento te gusta más escuchar?\n\t1) Violín\n\t2) Trompeta\n\t3) Piano\n\t4) Tambor\nOpción (1~4): "))
    if q3 != 1 and q3 != 2 and q3 != 3 and q3 != 4:
        print("Elige una opción correcta.\n")

if q1 == 1:
    gryffindor +=1
    ravenclaw +=1
else:
    hufflepuff +=1
    slytherin +=1

if q2 == 1:
    hufflepuff +=1
elif q2 == 2:
    slytherin +=1
elif q2 == 3:
    ravenclaw +=1
else:
    gryffindor +=1

if q3 == 1:
    slytherin +=1
elif q3 == 2:
    hufflepuff +=1
elif q3 == 3:
    ravenclaw +=1
else:
    gryffindor +=1

if slytherin > hufflepuff and slytherin > ravenclaw and slytherin > gryffindor:
    print("\nPerteneces a la casa de Slytherin")
elif hufflepuff > ravenclaw and hufflepuff > gryffindor:
    print("\nPerteneces a la casa de Hufflepuff")
elif ravenclaw > gryffindor:
    print("\nPerteneces a la casa de Ravenclaw")
else:
    print("\nPerteneces a la casa de Gryffindor")
print("\nFin.")