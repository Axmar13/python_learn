'''
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''

VALUES_GAMES = ["R", "r", "P", "p", "S", "s"]

def who_wins(data: list[tuple]) -> str:
    player_1, player_2 = 0, 0
    
    for row in data:
        if type(row) != tuple or len(row) != 2:
            return "Error"
        if (row[0] not in VALUES_GAMES) or (row[1] not in VALUES_GAMES):
            return "Error"
        c1 = row[0].upper()
        c2 = row[1].upper()
        if c1 != c2:
            if c1 == "R" and c2 == "S" or c1 == "S" and c2 == "P" or c1 == "P" and c2 == "R":
                player_1 += 1
            else:
                player_2 += 1
    if player_1 > player_2:
        return "Player 1"
    elif player_1 < player_2:
        return "Player 2"
    else:
        return "Tie"

print(who_wins([("R","S"), ("S","R"), ("P","R")]))
print(who_wins([("R","S"), ("S","R"), ("P","S")]))
print(who_wins([("R","S"), ("S","R"), ("P","P")]))