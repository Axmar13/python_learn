'''
 * Dado un listado de números, encuentra el SEGUNDO más grande.
'''

def find_second_largest(numbers: list):
    larger_num = 0
    descendent_list = []
    while len(numbers) > 0:
        aux = None
        for i in numbers:
            if aux is None:
                aux = i
            elif aux <= i:
                aux = i
        numbers.remove(aux)
        descendent_list.append(aux)
    return (descendent_list[1])

print(f"El segundo más grande es: {find_second_largest([9, 85, 22, 15, 42, 77])}")