'''
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
'''
NATURAL = '.-'
MORSE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....",
            "I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","Ñ":"--.--","O":"---",
            "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--",
            "X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--",
            "4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","·":".-.-.-",
            ",":"--..--","?":"..--..",'"':".-..-.","/":"-..-.", " ":"  "}

def morse_to_txt(data: str):
    code = data.split()
    for i in code:
        for key in MORSE:
            if MORSE[key] == i:
                print(key, end="")
    print()

def txt_to_morse(data: str):
    text = data.upper()
    for i in text:
        print(MORSE.get(i), end=" ")
    print()

data = input("Ingrese los datos a convertir: ")
if data[0] in NATURAL:
    morse_to_txt(data)
else:
    txt_to_morse(data)