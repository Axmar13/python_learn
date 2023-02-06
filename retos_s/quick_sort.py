'''
 * Enunciado: Implementa uno de los algoritmos de ordenación más famosos:
 * el "Quick Sort", creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia
 *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
 *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
 *   donde trabajaremos y entenderemos los más famosos de la historia.
'''

def quick_sort(numbers: list):
    if len(numbers) < 1:
        return []
    pivot = numbers[0]
    left = []
    right = []
    equal = []
    for num in numbers:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            right.append(num)
    return quick_sort(left) + equal + quick_sort(right)
        

array = [42, 64, 5, 81, 76, 75, 40, 51, 50, 71]
print(f"{array} -> {quick_sort(array)}")