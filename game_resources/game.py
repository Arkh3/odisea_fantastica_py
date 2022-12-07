import os
import random
import math
import yaml
from utils.utils import loadYaml, menu, captureKeys, flush_input
from datetime import datetime

HISTORY_PATH = os.path.join(os.path.dirname(__file__), "history")

# TRIVIA FUNCTIONS

# MONEY LAUNDERING FUNCTIONS

def turnGemsToCoins(gems):
    # TODO: FIGURE OUT THE EQUATION AND RETURN AN INTEGER
    ret = math.log(gems, 5)
    return ret

def moneyExchangeOffice():
    option = None

    while option != 'Salir':
        option = menu("OFICINA DE CAMBIO DE MONEDA:\n", ['Cambiar gemas a monedas', 'Salir'])

        if option == 'Cambiar gemas a monedas':
            os.system('cls')

            rightValue = False
            
            while not rightValue:
                flush_input()
                gemsInput = input('\n - GEMAS A CAMBIAR: ')

                try:
                    gems = int(gemsInput)

                    if gems < 0:
                        raise ValueError

                    rightValue = True
                except ValueError:
                    os.system('cls')
                    print('[El valor insertado debe ser un número natural]')
            
            coins = turnGemsToCoins(gems)

            print('\n  CAMBIO: ' + str(gems) + ' gemas = ' + str(coins) + " monedas")
            print("\n  Salir <")
            captureKeys(['enter'])

# TURN/HISTORY FUNCTIONS

def getRandomDirection():
    direction = random.randint(0,1)

    if direction == 0:
        return "Clockwise"
    else:
        return "Counter clockwise"

def getRandomDistance(min_distance = 1, max_distance=1):
    return random.randint(min_distance, max_distance)

def generateTurn(turnNumber, parameters):
    turn = {
        "number": turnNumber,
        "boss_values":[],
        "items_used":[]
    }

    for boss in parameters["bosses"]:
        boss_values = {
            "name": boss["display_name"],
            "ring_number": boss["ring"],
            "distance": getRandomDistance(max_distance=boss["max_movement"]),
            "direction": boss["direction"]
        }

        if boss["direction"] == "random":
            boss_values["direction"] = getRandomDirection()

        turn["boss_values"].append(boss_values)

    return turn

def turnToString(turn, isLatestTurn=False):
    ret = ""

    if not isLatestTurn:
        aux = "  Turno: " + str(turn["number"]) 
        aux2 = ''
    else:
        aux = "| Turno: " + str(turn["number"]) + " |"
        aux2 = " "

        for _ in range(len(aux) - 2):
            aux2 += "="

    
    ret += aux2 + "\n" + aux + "\n" + aux2 + "\n\n"


    for values in turn["boss_values"]:
        ret += str(values["ring_number"]) + ". " + values["name"] + "\n\n"
        ret += "   - Sentido: " + values["direction"] + "\n"
        ret += "   - Distancia: " + str(values["distance"]) + "\n"
        ret +=  "\n\n"

    return ret

def saveGame(history):
    filename = datetime.now().strftime("%d%m%Y_%H%M%S") + ".his"
    
    savePath = os.path.join(HISTORY_PATH, filename)

    print(savePath)

    with open(savePath, 'w') as outfile:
        yaml.dump(history, outfile, default_flow_style=False)

def getSavedGamesList():
    return os.listdir(HISTORY_PATH)

def getSavedGame(name):
    return loadYaml(os.path.join(HISTORY_PATH, name))

# MAIN FUNCTION

def startGame(hist=[]):
    parameters = loadYaml(os.path.join(os.path.dirname(__file__), "parameters.yaml"))
    
    history = hist

    actualTurn = len(history) + 1
    latestTurn = len(history) + 1
    history.append(generateTurn(latestTurn, parameters))

    option = None
    
    while option != 'Salir':
        # DISPLAY TURN AND CHOOSE OPTION

        if actualTurn == latestTurn:
            options = ["Nuevo turno", "Turno anterior", "Uso de item", "Oficina de cambio de moneda", "Salir"]
        else:
            options = ["Turno siguiente", "Turno anterior", "Ir al turno más reciente", "Salir"]

        option = menu(turnToString(history[actualTurn - 1], isLatestTurn=(latestTurn == actualTurn)), options)

        # HANDLE OPTIONS

        if option == "Nuevo turno":
            latestTurn += 1
            actualTurn = latestTurn
            history.append(generateTurn(latestTurn, parameters))

        elif option == "Turno anterior":
            if actualTurn != 1:
                actualTurn -= 1

        elif option == "Uso de item":
            pass

        elif option == "Oficina de cambio de moneda":
            moneyExchangeOffice()

        elif option == "Turno siguiente":
            actualTurn += 1

        elif option == "Ir al turno más reciente":
            actualTurn = latestTurn

        elif option == "Salir":
            confirm = menu("¿Seguro que quieres salir?\n", ['Si', 'No'])

            if confirm == 'No':
                option = None
            else:
                wantSave = menu("¿Quieres guardar la partida?\n", ['Si', 'No'])

                if wantSave == 'Si':
                    saveGame(history)
