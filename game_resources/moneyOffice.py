import os
import math
from utils.utils import menu, flush_input

def turnGemsToCoins(gems):
    ret = math.log(1 + (2*gems), 2)
    return math.ceil(ret)

def moneyExchangeOffice():
    officeSign = 'OFICINA DE CAMBIO DE MONEDA:'
    option = None

    while option != 'Salir':
        option = menu(officeSign + '\n', ['Cambiar gemas a monedas', 'Salir'])

        if option == 'Cambiar gemas a monedas':

            option2 = None
            while option2 != 'Salir':

                rightValue = False
            
                while not rightValue:
                    os.system('cls')
                    flush_input()

                    print(officeSign)
                    print('[El valor insertado debe ser un número natural]\n')
                    gemsInput = input(' - GEMAS A CAMBIAR: ')

                    try:
                        gems = int(gemsInput)

                        if gems < 0:
                            raise ValueError

                        rightValue = True
                    except ValueError:
                        pass
                
                coins = turnGemsToCoins(gems)

                questionHeader = officeSign + '\n\n Conversión -> ' + str(gems) + ' gemas = ' + str(coins) + ' monedas\n\n===================================\n'
                questionOptions = ['Otro cálCulo', 'Salir']

                option2 = menu(questionHeader, questionOptions)
