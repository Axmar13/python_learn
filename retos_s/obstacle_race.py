'''
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''

def race(action: list, track: str) -> bool:
    final_race = ""
    state_of_race = True
    if len(action) == len(track):
        for i in range(len(action)):
            if action[i] == "run" and track[i] == "_":
                final_race += "_"
            elif action[i] == "jump" and track[i] == "|":
                final_race += "|"
            elif action[i] == "run" and track[i] == "|":
                final_race += "/"
                state_of_race = False
            elif action[i] == "jump" and track[i] == "_":
                final_race += "x"
                state_of_race = False
            else:
                print("Los datos de la carrera son incorrectos")
        return state_of_race
    else:
        print("Los datos de la carrera no coindicen con los datos de la pista")
        
print(race(["run", "run", "jump", "run", "jump", "run"], "__|_|_"))
print(race(["run", "run", "jump", "run", "run", "run"], "__|_|_"))
print(race(["run", "run", "jump", "run", "run", "run"], "__|___"))
print(race(["run", "run", "jump", "run", "run", "jump"], "__|__|"))