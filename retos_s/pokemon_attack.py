'''
 * Enunciado: Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
'''

import os
#Datos sacados de la wiki
POKEMONS = {
    1: {"name": "Bulbasaur", "type": "Planta", "attack": 49, "defense": 49},
    2: {"name": "Charmander", "type": "Fuego", "attack": 52, "defense": 43},
    3: {"name": "Squirtle", "type": "Agua", "attack": 48, "defense": 65},
    4: {"name": "Pikachu", "type": "Eléctrico", "attack": 55, "defense": 40}
}

def menu(num: int = 0):
    con = 1
    for i in POKEMONS.values():
        if con != num:
            name = i.get("name")
            print(f"{con}){name}")
        con += 1

def damage_calculation(attacker: int, defender: int):
    effectiveness = effectiveness_calculation(attacker, defender)
    damage = 50 * (POKEMONS[attacker]["attack"] / POKEMONS[defender]["defense"]) * effectiveness
    attacker_name = POKEMONS[attacker]["name"]
    defender_name = POKEMONS[defender]["name"]
    print(f"\n*{attacker_name} le hizo {damage:.4} de daño a {defender_name}*")

def effectiveness_calculation(attacker: int, defender: int):
    attacker_type = POKEMONS[attacker]["type"]
    defender_type = POKEMONS[defender]["type"]
    if (attacker_type == "Planta" and defender_type == "Agua") or (attacker_type == "Fuego" and defender_type == "Planta") or (attacker_type == "Agua" and defender_type == "Fuego") or (attacker_type == "Eléctrico" and defender_type == "Agua"):
        effectiveness = 2
    elif (attacker_type == "Planta" and defender_type == "Eléctrico") or (attacker_type == "Fuego" and defender_type == "Eléctrico"):
        effectiveness = 1
    else:
        effectiveness = 0.5
    return effectiveness

print("***Ataque Pokemón***")
menu()
choice = 0
while choice not in POKEMONS.keys():
    choice = int(input("¿Qué pokemón desea que sea el atacante? "))
    if choice not in POKEMONS.keys():
        os.system("cls")
        print("Elija una opción válida.\n")
        menu()
attacker = choice
print()
while choice not in POKEMONS.keys() or choice == attacker:
    menu(attacker)
    choice = int(input("¿Qué pokemón desea que sea el defensor? "))
    if choice not in POKEMONS.keys() or choice == attacker:
        os.system("cls")
        print("Elija una opción válida.\n")
defender = choice
damage_calculation(attacker, defender)