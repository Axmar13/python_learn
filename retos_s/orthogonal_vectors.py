'''
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''

def check_orthogonal(data: list[list]):
    if len(data[0]) == len(data[1]):    
        a1, a2, b1, b2 = data[0][0], data[0][1], data[1][0], data[1][1]
        result = (a1 * b1) + (a2 * b2)
        if result == 0:
            return "Los vectores son hortogonales"
        else:
            return "Los vectores no son hortogonales"
    else:
        return "Error, los vectores no tienen la misma logitud."


print(check_orthogonal([[1, -2], [3, 6]]))
print(check_orthogonal([[13, 4], [-8, -5]]))
print(check_orthogonal([[13, 13], [-13, 13]]))
