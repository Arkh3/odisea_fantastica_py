import os
import math
from utils.utils import menu, flush_input

OFFICE_SIGN = 'OFICINA DE CAMBIO DE MONEDA:'

def turnGemsToCoins(gems):
    ret = math.log(1 + (2*gems), 2)
    return math.ceil(ret)

def exchangeGemsForCoins():
    option = None
    while option != 'Salir':

        rightValue = False
    
        while not rightValue:
            os.system('cls')
            flush_input()

            print(OFFICE_SIGN)
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

        questionHeader = OFFICE_SIGN + '\n\n Conversión -> ' + str(gems) + ' gemas = ' + str(coins) + ' monedas\n\n===================================\n'
        questionOptions = ['Otro cálCulo', 'Salir']

        option = menu(questionHeader, questionOptions)

def moneyExchangeOffice():
    
    option = None

    while option != 'Salir':
        option = menu(OFFICE_SIGN + '\n', ['Cambiar gemas a monedas', 'Salir'], markedOption=option)

        if option == 'Cambiar gemas a monedas':
            exchangeGemsForCoins()
