'''
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
'''
# Diccionario con los tipos de paréntesis
PARENTHESIS = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def balanced_expression(expression: str):
    # Lista de paréntesis en la expresión
    expression_par = []

    # Crea un diccionario invertido, con las llaves de cierre como llave
    inverted_par = {value: key for key, value in PARENTHESIS.items()}
    
    # Variable para definir si una expresión está equilibrada
    its_balanced = True

    # Por cada letra de la expresión, añade las llaves de apertura a una lista
    #   - Verifica si un paréntesis es cerrado de forma correcta
    #       * Si NO es cerrado de forma correcta, vuelve False its_balanced
    #       * Si ES cerrado de forma correcta, elimina el símbolo de apertura de la lista
    for letter in expression:
        # Verifica si la letra es un paréntesis de apertura, para añadirlo a la lista
        if letter in PARENTHESIS.keys():
            expression_par.append(letter)

        # Si la letra está dentro de los símbolos de cierre y coincide con el último valor de la lista, lo extrae
        elif letter in PARENTHESIS.values() and inverted_par[letter] == expression_par[-1]:
            expression_par.pop()

        # Si la letra está en los símbolos de cierre, y no se encuentra abierto, define la expresión no balanceada
        elif letter in PARENTHESIS.values():
            its_balanced = False

    # Si se encuentran valores en la lista, la expresión no está balanceada
    if len(expression_par) > 0:
        its_balanced = False

    # Imprime el resultado de la expresión
    print(f"The expression '{expression}' {'is' if its_balanced else 'is not'} balanced")


# Test
balanced_expression("{ [ a ( c + d ) ] - 5 }")
balanced_expression("{ a ( c + d ) ] - 5 }")
balanced_expression("{ [}(])")
balanced_expression("{[()]}")
balanced_expression("{[()]")