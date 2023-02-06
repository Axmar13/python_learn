'''
 * Enunciado: Dado un array de enteros ordenado y sin repetidos, 
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
'''

def check_array(array: list) -> bool:
    #Verifico que los números sean enteros y estén ordenados
    num = array[0]
    con1, con2 = 0, 0
    for i in array:
        if type(i) != int:
            return True
        if num > i:
            con1 += 1
        elif num < i:
            con2 += 1
        num = i
    if con1 > 0 and con2 > 0:
        return True
    #Verifico que los números no estén repetidos
    for i in array:
        if array.count(i) > 1:
            return True
    return False

def add_lost_numbers(numbers: list):
    num, con = None, 1
    error = check_array(numbers)
    if error == True:
        return "Los números no son enteros, no se encuentran ordenados o se encuentran repetidos."
    else:
    #Agrego los números que faltan entre el menor y el mayor
        if numbers[0] < numbers[-1]:
            num = numbers[0]
            while num < numbers[-1]:
                num += 1
                if num not in numbers:
                    numbers.insert(con, num)
                con += 1
        else:
            num = numbers[0]
            while num > numbers[-1]:
                num -= 1
                if num not in numbers:
                    numbers.insert(con, num)
                con += 1
    return numbers


print(add_lost_numbers([1, 2, 3, 4, 7]))
print(add_lost_numbers([7, 4, 3, 2, 1]))
print(add_lost_numbers([5, 17, 87, 92, 99]))
print(add_lost_numbers([5, 13, 26, 39, 52]))
print(add_lost_numbers([5, 92, 17, 99, 87]))
print(add_lost_numbers([5, 99, 17, 99, 87]))
print(add_lost_numbers([1, 2, 3.13, 4, 7]))