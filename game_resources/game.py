import os
import random
from utils.utils import loadYaml, menu, storeYaml, captureKeys
from datetime import datetime
from .triviaOffice import triviaQuestionsOffice
from .moneyOffice import moneyExchangeOffice
from .itemOffice import itemManagementOffice, showExpiredItems

HISTORY_PATH = os.path.join(os.path.dirname(__file__), 'history')

def getRandomDirection():
    direction = random.randint(0,1)

    if direction == 0:
        return 'Clockwise'
    else:
        return 'Counter clockwise'

def getRandomDistance(min_distance = 1, max_distance=1):
    return random.randint(min_distance, max_distance)

def generateTurn(turnNumber, parameters):
    turn = {
        'number': turnNumber,
        'boss_values':[],
        'items_used':[]
    }

    for boss in parameters['bosses']:
        boss_values = {
            'name': boss['display_name'],
            'ring_number': boss['ring'],
            'distance': getRandomDistance(max_distance=boss['max_movement']),
            'direction': boss['direction']
        }

        if boss['direction'] == 'random':
            boss_values['direction'] = getRandomDirection()

        turn['boss_values'].append(boss_values)

    return turn

def turnToString(turn, isLatestTurn=False):
    ret = ''

    if not isLatestTurn:
        aux = '  Turno: ' + str(turn['number']) 
        aux2 = ''
    else:
        aux = '| Turno: ' + str(turn['number']) + ' |'
        aux2 = ' '

        for _ in range(len(aux) - 2):
            aux2 += '='

    
    ret += aux2 + '\n' + aux + '\n' + aux2 + '\n\n'

    for values in turn['boss_values']:
        ret += "    " + str(values['ring_number']) + '. ' + values['name'] + '\n\n'
        ret += '  - Sentido: ' + values['direction'] + '\n'
        ret += '  - Distancia: ' + str(values['distance']) + '\n'
        ret +=  '\n'

    return ret

def getSavedGamesList():
    return os.listdir(HISTORY_PATH)

def getSavedGame(name):
    return loadYaml(os.path.join(HISTORY_PATH, name))

def saveGame(header, history):
    confirmSave = menu(header + '¿Quieres guardar la partida?\n', ['Si', 'No'])

    if confirmSave == 'Si':
        filename = datetime.now().strftime('Fecha %d-%m-%Y Hora %H_%M_%S') + '.his'
        savePath = os.path.join(HISTORY_PATH, filename)

        storeYaml(history, savePath)

        print("\nLa partida se ha guardado correctamente.\n")
        print("Presiona [ENTER] para continuar...")
        captureKeys(['enter'])

# MAIN FUNCTION

def startGame(hist):

    history = hist
    
    try:
        parameters = loadYaml(os.path.join(os.path.dirname(__file__), 'parameters.yaml'))

        actualTurn = len(history)
        latestTurn = len(history)

        if len(history) == 0:
            actualTurn += 1
            latestTurn += 1
            history.append(generateTurn(latestTurn, parameters))

        option = None
        
        while option != 'Salir':
            # DISPLAY TURN AND CHOOSE OPTION
            if actualTurn == latestTurn:
                options = ['Nuevo turno', 'Turno anterior', 'Oficina de Gestión de Items', 'Oficina de Cambio de Moneda', 'Oficina Preguntas Tormentosas', 'Salir']
            else:
                options = ['Turno siguiente', 'Turno anterior', 'Ir al turno más reciente', 'Salir']

            option = menu(turnToString(history[actualTurn - 1], isLatestTurn=(latestTurn == actualTurn)), options, markedOption=option, confirmOptions='Salir')

            # HANDLE OPTIONS
            if option == 'Nuevo turno':
                latestTurn += 1
                actualTurn = latestTurn
                history.append(generateTurn(latestTurn, parameters))
                showExpiredItems(history)

            elif option == 'Turno anterior':
                if actualTurn != 1:
                    actualTurn -= 1

            elif option == 'Turno siguiente':
                actualTurn += 1

            elif option == 'Ir al turno más reciente':
                actualTurn = latestTurn

            elif option == 'Oficina de Gestión de Items':
                history = itemManagementOffice(history)

            elif option == 'Oficina de Cambio de Moneda':
                moneyExchangeOffice()

            elif option == 'Oficina Preguntas Tormentosas':
                triviaQuestionsOffice()

            elif option == 'Salir':
                saveGame('', history)
    
    except Exception as e:
        saveGame('ALGO NO HA SALIDO COMO ESPERABA\n\n Se va a cerrar el programa ', history)
        raise e