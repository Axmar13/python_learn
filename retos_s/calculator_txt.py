'''
 * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones.
'''

VALID_OPERATORS = ["+", "-", "*", "/"]

def read_txt(path: str):
    total_list = []
    nums = []
    operators = []

    with open(path, "r") as file:
        file_items = file.readlines()

    for item in file_items:
        new_item = item.replace("\n", '')
        try:
            new_item = float(new_item)
            nums.append(new_item)
        except:
            if new_item != "":
                operators.append(new_item)
        finally:
            if new_item != "":
                total_list.append(new_item)

    file.close()

    return total_list, nums, operators

    

def calculator(path: str):
    total_list, number_list, operator_list = read_txt(path=path)
    result = number_list[0]
    balance = 0    
    
    for char in total_list:
        if type(char) == float:
            balance += 1
        
        elif type(char) == str:
            if char in VALID_OPERATORS:
                balance -= 1
       
        if not 0 <= balance <= 1:
            print(f"Error en {char}")
            break
   
    if balance != 1:
        return "Error"
   
    for i in range(len(operator_list)):
        if operator_list[i] == "+":
            result += number_list[i+1]

        elif operator_list[i] == "-":
            result -= number_list[i+1]

        elif operator_list[i] == "/":
            result /= number_list[i+1]

        elif operator_list[i] == "*":
            result *= number_list[i+1]

    print(f"The result is '{result}'")

calculator("retos_s/Challenge21.txt")