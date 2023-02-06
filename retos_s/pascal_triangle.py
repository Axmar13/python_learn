'''
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
 * indicándole únicamente el tamaño del lado.
 *
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
'''

#Solución obtenida de https://geekflare.com/es/pascals-triangle-in-python/#:~:text=C%C3%B3mo%20construir%20el%20tri%C3%A1ngulo%20de%20Pascal%20con%20el%20n%C3%BAmero%20dado,r!

def pascal_triangle(side: int):
    if side == 1:
        return [[1]]
    else:
        res_arr = pascal_triangle(side - 1)
        cur_row = [1]
        prev_row = res_arr[-1]
        print(prev_row)
        for i in range(len(prev_row)-1):
            cur_row.append(prev_row[i] + prev_row[i+1]) 
        cur_row += [1]
        res_arr.append(cur_row)
        print(res_arr)
        return res_arr

triangle_list = pascal_triangle(4)

for i,row in enumerate(triangle_list):
    for j in range(len(triangle_list) - i + 1):
        print(end=" ")
    for j in row:
        print(j, end=" ")
    print("\n")