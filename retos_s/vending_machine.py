'''
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''

#Para acceder al producto y a su precio como datos se puede hacer un diccionario de diccionarios
#En vez de comprobar las monedas mediante cálculo se puede comprobar más fácil colocando las monedos dentro de una lista y recorriendo la misma


import os, time
inv = {"Coca-Cola": 10, "Sprite": 10, "Pepsi": 10, "Seven-Up": 10, "Schweppes(T)": 10, "Schweppes(P)": 10, "Agua": 10}

def menu():
    print("~~~~~~~~~~~~~~~~~~~~\n~ Vending Maching ~\n~~~~~~~~~~~~~~~~~~~~")
    print("1)200$ Coca-Cola\n2)200$ Sprite\n3)150$ Pepsi\n4)150$ Seven-Up\n5)100$ Schweppes (Tónica)\n6)100$ Schweppes (Pomelo)\n7)50$ Agua Mineral")

def eject_money(total_money: int):
    con = 0
    while con < 3:
        con += 1
        print("Expulsando dinero... Ingrese dinero soportado por la máquina!")
        time.sleep(2)
        os.system("cls")
        time.sleep(1)
    total_money = 0
    return total_money

def eject_change(total_money: int):
    con = 0
    while con < 3:
        con += 1
        print(f"Expulsando {total_money}$... Agarre su vuelto!")
        time.sleep(2)
        os.system("cls")
        time.sleep(1)
    total_money = 0
    return total_money

def execute_choice(choice: int, money: int):
    os.system("cls")
    con = 0
    if choice == 1:
        if inv["Coca-Cola"] > 0 and money >= 200:
            money = 200 - money
            inv["Coca-Cola"] -= 1
            print(f"Disfrute su Coca-Cola")
            time.sleep(3)
            os.system("cls")
        elif inv["Coca-Cola"] == 0:
            print("No quedan existencias de Coca-Cola")
        else:
            while con < 3:
                print(f"Faltan {200 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    elif choice == 2:
        if inv["Sprite"] > 0 and money >= 200:
            money = 200 - money
            inv["Sprite"] -= 1
            print(f"Disfrute su Sprite")
            time.sleep(3)
            os.system("cls")
        elif inv["Sprite"] == 0:
            print("No quedan existencias de Sprite")
        else:
            while con < 3:
                print(f"Faltan {200 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    elif choice == 3:
        if inv["Pepsi"] > 0 and money >= 150:
            money = 150 - money
            inv["Pepsi"] -= 1
            print(f"Disfrute su Pepsi")
            time.sleep(3)
            os.system("cls")
        elif inv["Pepsi"] == 0:
            print("No quedan existencias de Pepsi")
        else:
            while con < 3:
                print(f"Faltan {150 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    elif choice == 4:
        if inv["Seven-Up"] > 0 and money >= 150:
            money = 150 - money
            inv["Seven-Up"] -= 1
            print(f"Disfrute su Seven-Up")
            time.sleep(3)
            os.system("cls")
        elif inv["Seven-Up"] == 0:
            print("No quedan existencias de Seven-Up")
        else:
            while con < 3:
                print(f"Faltan {150 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    elif choice == 5:
        if inv["Schweppes(T)"] > 0 and money >= 100:
            money = 100 - money
            inv["Schweppes(T)"] -= 1
            print(f"Disfrute su Schweppes (Tónica)")
            time.sleep(3)
            os.system("cls")
        elif inv["Schweppes(T)"] == 0:
            print("No quedan existencias de Schweppes (Tónica)")
        else:
            while con < 3:
                print(f"Faltan {100 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    elif choice == 6:
        if inv["Schweppes(P)"] > 0 and money >= 100:
            money = 100 - money
            inv["Schweppes(P)"] -= 1
            print(f"Disfrute su Schweppes (Pomelo)")
            time.sleep(3)
            os.system("cls")
        elif inv["Schweppes(P)"] == 0:
            print("No quedan existencias de Schweppes (Pomelo)")
        else:
            while con < 3:
                print(f"Faltan {100 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    elif choice == 7:
        if inv["Agua"] > 0 and money >= 50:
            money = 50 - money
            inv["Agua"] -= 1
            print(f"Disfrute su Agua mineral")
            time.sleep(3)
            os.system("cls")
        elif inv["Agua"] == 0:
            print("No quedan existencias de Agua mineral")
        else:
            while con < 3:
                print(f"Faltan {50 - money}$")
                time.sleep(2)
                os.system("cls")
                time.sleep(1)
                con += 1
    else:
        return "Error"
    if money != 0:
        money = eject_change(money)
    return money


state,total_money, money = True, 0, 0
while state:
    error, money_flag = False, True
    while not error:
        while money_flag:
            menu()
            if money == 0:
                money = int(input("Ingrese dinero: "))
            else:
                money = int(input(f"Ingrese dinero ({total_money}): "))

            if money < 5 or money % 5 != 0 or money > 200:
                os.system("cls")
                error = True
                total_money = eject_money(total_money=total_money)
                money = 0
                continue
            else:
                total_money += money

            while state:
                choice = int(input("¿Desea ingresar más dinero?\n1)Sí\t2)No\t: "))
                if choice != 1 and choice != 2:
                    os.system("cls")
                    print("Ingrese una opción valida (1-2)\n")
                else:
                    state = False
            state = True
            if choice == 2:
                money_flag = False

        while state:    
            menu()
            print(f"Dinero: {total_money}$")
            choice = int(input("¿Qué producto desea comprar?: "))
            if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7:
                print("Ingrese una opción válida (1-7)\n")
            else:
                state = False
        state = True

        total_money = execute_choice(choice, total_money)

''' Solución de Oscar
# Productos de la máquina expendedora
PRODUCTS = {
    1: {"name": "Coca-Cola 350 ml", "price": 150},
    2: {"name": "Coca-Cola 500 ml", "price": 250},
    3: {"name": "Milk 120 ml", "price": 120},
    4: {"name": "Pizza small", "price": 500},
    5: {"name": "Sandwich", "price": 420},
    6: {"name": "Cereal", "price": 80},
    7: {"name": "Chocolate", "price": 360},
    8: {"name": "Water 500 ml", "price": 200},
    9: {"name": "Candy", "price": 30},
    10: {"name": "Yogurth", "price": 70}
}

# Monedas soportadas
COINS = [200, 100, 50, 10, 5]


def cashback_coins(cashback: int):
    coin_return = []
    cashback_total = cashback
    index = 0

    while cashback_total > 0:
        value_coin = COINS[index]

        if cashback_total >= value_coin:
            cashback_total -= value_coin
            coin_return.append(value_coin)

        if cashback_total < value_coin:
            index += 1

    return coin_return


def expendor_machine(coins: list[int], item: int):

    # Define si el producto está disponible en la máquina y el formato de las monedas ingresadas es correcto
    product_available = True if item in PRODUCTS.keys() else False
    coins_allowed = True
    [coins_allowed := False for coin in coins if coin not in COINS]

    if product_available and coins_allowed:
        # Obtiene el precio y nombre del producto
        product_item = PRODUCTS.get(item)
        product_price = product_item.get("price")
        product_name = product_item.get("name")

        # Define el total de monedas ingresadas
        total_cash = 0

        for coin in coins:
            total_cash += coin

        # Define si se tiene el dinero necesario para comprar
        if total_cash >= product_price:

            # Define la diferencia de dinero como cashback
            cashback = total_cash - product_price

            # Imprime la
            print(f"Retire '{product_name}' del dispensador.")

            if cashback == 0:
                print("No hay vuelto. Gracias por su compra!\n")

            else:
                # Determina las monedas a retornar
                cashback_moneys = cashback_coins(cashback)
                print(
                    f"Aquí está su vuelto {cashback_moneys}. Gracias por su compra!\n")

        else:
            # Define respuestas para
            print(
                f"Faltan {product_price - total_cash} centavos para comprar '{product_name}'.")
            print(f"Sus monedas {coins} son devueltas.\n")

    else:
        print("La opción ingresada no existe o no fueron ingresadas monedas permitidas\n")


# Tests
# (1)
expendor_machine(coins=[5, 10], item=9)

# (2)
expendor_machine(coins=[5, 100, 200], item=7)

# (3)
expendor_machine(coins=[100, 100, 100, 200], item=4)

# (4)
expendor_machine(coins=[100, 100, 100, "200"], item=4)

# (5)
expendor_machine(coins=[100, 100, 100, 200], item=23)
'''