'''
 * Enunciado: Crea un función, que dado un año, indique el elemento 
 * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos
 *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 *   (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
'''

JIA_ZI = {
    1: {"animal": "Rat", "element": "Wood"},
    2: {"animal": "Ox", "element": "Wood"},
    3: {"animal": "Tiger", "element": "Fire"},
    4: {"animal": "Rabbit", "element": "Fire"},
    5: {"animal": "Dragon", "element": "Earth"},
    6: {"animal": "Snake", "element": "Earth"},
    7: {"animal": "Horse", "element": "Metal"},
    8: {"animal": "Shepp", "element": "Metal"},
    9: {"animal": "Monkey", "element": "Water"},
    10: {"animal": "Rooster", "element": "Water"},
    11: {"animal": "Dog", "element": "Wood"},
    12: {"animal": "Pig", "element": "Wood"},
    13: {"animal": "Rat", "element": "Fire"},
    14: {"animal": "Ox", "element": "Fire"},
    15: {"animal": "Tiger", "element": "Earth"},
    16: {"animal": "Rabbit", "element": "Earth"},
    17: {"animal": "Dragon", "element": "Metal"},
    18: {"animal": "Snake", "element": "Metal"},
    19: {"animal": "Horse", "element": "Water"},
    20: {"animal": "Shepp", "element": "Water"},
    21: {"animal": "Moneky", "element": "Wood"},
    22: {"animal": "Rooster", "element": "Wood"},
    23: {"animal": "Dog", "element": "Fire"},
    24: {"animal": "Pig", "element": "Fire"},
    25: {"animal": "Rat", "element": "Earth"},
    26: {"animal": "Ox", "element": "Earth"},
    27: {"animal": "Tiger", "element": "Metal"},
    28: {"animal": "Rabbit", "element": "Metal"},
    29: {"animal": "Dragon", "element": "Water"},
    30: {"animal": "Snake", "element": "Water"},
    31: {"animal": "Horse", "element": "Wood"},
    32: {"animal": "Shepp", "element": "Wood"},
    33: {"animal": "Monkey", "element": "Fire"},
    34: {"animal": "Rooster", "element": "Fire"},
    35: {"animal": "Dog", "element": "Earth"},
    36: {"animal": "Pig", "element": "Earth"},
    37: {"animal": "Rat", "element": "Metal"},
    38: {"animal": "Ox", "element": "Metal"},
    39: {"animal": "Tiger", "element": "Water"},
    40: {"animal": "Rabbit", "element": "Water"},
    41: {"animal": "Dragon", "element": "Wood"},
    42: {"animal": "Snake", "element": "Wood"},
    43: {"animal": "Horse", "element": "Fire"},
    44: {"animal": "Shepp", "element": "Fire"},
    45: {"animal": "Monkey", "element": "Earth"},
    46: {"animal": "Rooster", "element": "Earth"},
    47: {"animal": "Dog", "element": "Metal"},
    48: {"animal": "Pig", "element": "Metal"},
    49: {"animal": "Rat", "element": "Water"},
    50: {"animal": "Ox", "element": "Water"},
    51: {"animal": "Tiger", "element": "Wood"},
    52: {"animal": "Rabbit", "element": "Wood"},
    53: {"animal": "Dragon", "element": "Fire"},
    54: {"animal": "Snake", "element": "Fire"},
    55: {"animal": "Horse", "element": "Earth"},
    56: {"animal": "Shepp", "element": "Earth"},
    57: {"animal": "Monkey", "element": "Metal"},
    58: {"animal": "Rooster", "element": "Metal"},
    59: {"animal": "Dog", "element": "Water"},
    60: {"animal": "Pig", "element": "Water"}
}

def check_year(year: int):
    original_year = year
    while year - 1983 > 60:
        year = year - 60
    data = JIA_ZI.get(year - 1983)
    animal = data.get("animal")
    element = data.get("element")
    print(f"El año {original_year} corresponde a 'Animal: {animal} ; Element: {element}'") 

check_year(2295)
check_year(2027)
check_year(2157)
check_year(2258)