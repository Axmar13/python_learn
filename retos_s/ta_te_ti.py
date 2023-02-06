'''
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
'''

CHARS_ACCEPTED = ["o", "x", "O", "X", ""]

def check_chars(matrix: list[list[str]]):
    chars_ok = True
    count_X = 0
    count_O = 0
    count_blank = 0

    for row in matrix:
        for char in row:
            if char in CHARS_ACCEPTED:
                if char.upper == "X":
                    count_X += 1
                elif char.upper == "O":
                    count_O += 1
                elif char == "":
                    count_blank += 1
            else:
                chars_ok = False

    #4- Comprobar si el tablero está vacio
    if count_blank == 9:
        chars_ok = False

    return chars_ok, count_X, count_O

def row_check(matrix: list[list[str]]):
    win_X = False
    win_O = False

    for row in matrix:
        if row.count("X") == 3 or row.count("x") == 3:
            win_X = True
        if row.count("O") == 3 or row.count("o") == 3:
            win_O = True

    return win_X, win_O

def tic_tac_toe(matrix: list[list[CHARS_ACCEPTED]]):

    #1- Comprobar cantidad de filas en la matriz
    if len(matrix) != 3:
        return None

    #2- Comprobar cantidad de columnas en la matriz
    for row in matrix:
        if len(row) != 3:
            return None
    
    #3- Comprobar que los caracteres sean los aceptados y contar la cantidad de 'X' y 'O'
    chars_ok, count_X, count_O = check_chars(matrix)

    if chars_ok == False:
        return None
    
    #5- Invertir las columnas en filas
    colum_elements = [[matrix[i][item] for i in range(3)] for item in range(3)]

    #6- Comprobar si hay ganadores en filas y columnas
    win_X_row, win_O_row = row_check(matrix)
    win_X_col, win_O_col = row_check(colum_elements)

    #7- Obtener y comprobar si hay ganadores en las diagonales
    diagonal_elements = [[matrix[i][i] for i in range(3)], [matrix[i][-i-1] for i in range(3)]]
    win_X_diag, win_O_diag = row_check(diagonal_elements)

    win_X = win_X_col or win_X_diag or win_X_row
    win_O = win_O_col or win_O_diag or win_O_row

    #8- Comprobar la diferencia de turnos y el posible empate
    if win_X == win_O or not -1 <= count_X - count_O <= 1 or count_O == 0 or count_X == 0:
        return None
    elif win_O:
        return "O"
    elif win_X:
        return "X"
    else:
        return "Empate"

# Tests
tic_tac_toe([
    ["O", "X", "O"], 
    ["O", "X", "O"], 
    ["O", "X", "O"]]) # -> None

tic_tac_toe([
    ["O", "O", "X"], 
    ["O", "X", "O"], 
    ["X", "X", "O"]]) # -> X

tic_tac_toe([
    ["X", "X", "O"], 
    ["O", "O", "X"], 
    ["X", "O", "X"]]) # -> Empate

tic_tac_toe([
    ["x", "X", ""], 
    ["O", "O", "o"], 
    ["X", "O", "X"]]) # -> O

tic_tac_toe([
    ["", "", ""], 
    ["", "x", ""], 
    ["", "", ""]]) # -> None

tic_tac_toe([
    ["O", "o", "o"]]) # -> None