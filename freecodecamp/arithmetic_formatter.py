'''import re

errors_dic = {
    'error1': "Error: Too many problems.",
    'error2': "Error: Operator must be '+' or '-'.",
    'error3': "Error: Numbers must only contain digits.",
    'error4': "Error: Numbers cannot be more than four digits."
    }


def arithmetic_arranger(data: list, answer = False) -> str:
    error: str
    if len(data) > 5:
        error = errors_dic["error1"]
        return error
    
    first = ""
    second = ""
    lines = ""
    result_line = ""
    string = ""

    for operations in data:
        if (re.search("[^\s0-9.+-]", operations)):
            if (re.search("[/]", operations) or re.search("[*]",operations)):
                error = errors_dic["error2"]
                return error
            error = errors_dic["error3"]
            return error
        
        dig1 = operations.split(" ")[0]
        dig2 = operations.split(" ")[2]
        operator = operations.split(" ")[1]

        if len(dig1) > 4 or len(dig2) > 4:
            error = errors_dic["error4"]
            return error
        
        if operator == "+":
            result = str(int(dig1) + int(dig2))
        elif operator == "-":
            result = str(int(dig1) - int(dig2))
        
        length = max(len(dig1), len(dig2)) + 2
        top = str(dig1).rjust(length)
        bottom = operator + str(dig2).rjust(length - 1)
        line = ""
        for _ in range(length):
            line += "-"
        
        if operations != data[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            result_line += result + "    "
        else:
            first += top
            second += bottom
            lines += line
            result_line += result
        
    if answer:
        string = first + "\n" + second + "\n" + lines + "\n" + result_line
    else:
        string = first + "\n" + second + "\n" + lines
    return string

#print(arithmetic_arranger(["32 + 698"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
'''

def solucionarRompecabezas(n):
    a = 1
    b = 1
    c = 1
    d = 1
    resultado = 0

    for i in range(n):
        resultado = 3 * d + 1 * c + 4 * b + 1 * a
        a = b
        b = c
        c = d
        d = resultado
    print(resultado)
    return d % 10000000000


print(solucionarRompecabezas(10))
print(solucionarRompecabezas(100))
print(solucionarRompecabezas(2023**100))