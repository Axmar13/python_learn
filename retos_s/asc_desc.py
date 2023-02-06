'''
 * Crea una función que ordene y retorne una 'matriz' de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
'''


def sort_list(numbers_list: list, trend: str):
    if trend == "Asc":
        ascendent_list = []
        while len(numbers_list) > 0:
            aux = None
            for i in numbers_list:
                if aux is None:
                    aux = i
                elif aux >= i:
                    aux = i
            numbers_list.remove(aux)
            ascendent_list.append(aux)
        return ascendent_list
    else:
        descendent_list = []
        while len(numbers_list) > 0:
            aux = None
            for i in numbers_list:
                if aux is None:
                    aux = i
                elif aux <= i:
                    aux = i
            numbers_list.remove(aux)
            descendent_list.append(aux)
        return descendent_list


print(sort_list([2, 13, 7, 9, 4, 14, 6], "Asc"))
print(sort_list([2, 13, 7, 9, 4, 14, 6], "Desc"))
