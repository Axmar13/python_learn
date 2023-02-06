'''
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
'''

def check_common_chars(string1: str, string2: str):
    out_string1 = string1.lower()
    out_string2 = string2.lower()
    common_chars_list = []
    for char in out_string1:
        if char in out_string2 and char != " ":
            common_chars_list.append(char)
    for char in common_chars_list:
        out_string1 = out_string1.replace(char, "")
        out_string2 = out_string2.replace(char, "")

    print(f"For '{string1}' the output is: '{out_string1}'")
    print(f"For '{string2}' the output is: '{out_string2}'")

check_common_chars(input("Ingrese una frase: "), input("Ingrese otra frase: "))