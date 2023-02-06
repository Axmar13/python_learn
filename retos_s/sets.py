'''
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
'''

def common_chars(list1: list, list2: list, state: bool) -> list:
    new_list = list()
    lenght_list = 0

    if state == True:
        if len(list1) >= len(list2):
            for item in list1:
                if item in list2:
                    new_list.append(item)
        else:
            for item in list2:
                if item in list1:
                    new_list.append(item)
    else:
        for item in list1:
            if item in list2:
                continue
            else:
                new_list.append(item)
        for item in list2:
            if item in list1:
                continue
            else:
                new_list.append(item)            
    return new_list


print(common_chars([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8], True))
print(common_chars([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8], False))


''' Solución de Oscar

def compare_list(list_one: list, list_two: list, compare: bool):

    # Determina los elementos comunes y no comunes de dos listas.
    # * Con los elementos no comunes se evalúan ambas listas.
    common = [i for i in list_one if i in list_two]
    uncommon = [i for i in list_one if i not in list_two]
    uncommon.extend([i for i in list_two if i not in list_one])

    # Si el booleano es True, retorna los elementos comunes
    if compare == True:
        return common

    # En caso de que sea False, retorna los elementos no comunes
    elif compare == False:
        return uncommon

    # En cualquier otro caso, retorna None
    else:
        return None


# Tests
print(compare_list([1, 2, 3], [3, "4", 5], True))
print(compare_list([1, 2, 3], [3, "4", 5], False))
print(compare_list([1, "g", "3", 6, 7], ["3", "g", 5], True))
print(compare_list([1, "g", "3", 6, 7], ["3", "g", 5], False))
print(compare_list([1, 2, 3], [3, 4, 5, 8, 9], True))
print(compare_list([1, 2, 3], [3, 4, 5, 8, 9], False))

'''