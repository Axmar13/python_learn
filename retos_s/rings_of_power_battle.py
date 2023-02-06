'''
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
'''

import random

KINDHEARTED = {
    "Pelosos": 1,
    "Sureños buenos": 2,
    "Enanos": 3,
    "Númenóreanos": 4,
    "Elfos": 5
}

EVILS = {
    "Sureños malos": 2,
    "Orcos": 2,
    "Goblins": 2,
    "Huargos": 3,
    "Trolls": 5,
}

def army_set():
    kindhearted_army = {}
    for key in KINDHEARTED:
        kindhearted_army[key] = random.randint(0, 1000)
    evils_army = {}
    for key in EVILS:
        evils_army[key] = random.randint(0, 1000)
    caclulate_battle(kindhearted_army, evils_army)

def caclulate_battle(kindhearted_army: dict, evils_army: dict):
    kindhearted_points, evils_points = 0, 0
    for key in kindhearted_army:
        if key == "Pelosos":
            kindhearted_points += kindhearted_army[key]
        elif key == "Sureños buenos":
            kindhearted_points += kindhearted_army[key] * 2
        elif key == "Enanos":
            kindhearted_points += kindhearted_army[key] * 3
        elif key == "Númenóreanos":
            kindhearted_points += kindhearted_army[key] * 4
        elif key == "Elfos":
            kindhearted_points += kindhearted_army[key] * 5
    for key in evils_army:
        if key == "Sureños malos":
            evils_points += evils_army[key] * 2
        elif key == "Orcos":
            evils_points += evils_army[key] * 2
        elif key == "Goblins":
            evils_points += evils_army[key] * 2
        elif key == "Huargos":
            evils_points += evils_army[key] * 3
        elif key == "Trolls":
            evils_points += evils_army[key] * 5
    result = kindhearted_points - evils_points
    if result < 0:
        result = result * -1
        print(f"Ganaron las razas malvadas con un total de {evils_points} puntos por sobre las razas bondadosas las cuales contaban con un total de {kindhearted_points} puntos.")
    else:
        print(f"Ganaron las razas bondadosas con un total de {kindhearted_points} puntos por sobre las razas malvadas las cuales contaban con un total de {evils_points} puntos.")
    print("Estadísticas: ")
    print("Ejército malvado: ")
    for key in evils_army:
        print(f"{key}: {evils_army[key]}")
    print("Ejército bondadoso:")
    for key in kindhearted_army:
        print(f"{key}: {kindhearted_army[key]}")

army_set()