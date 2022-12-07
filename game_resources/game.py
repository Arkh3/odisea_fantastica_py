import os
import random
import math
import yaml
from utils.utils import loadYaml, menu, captureKeys, flush_input
from datetime import datetime

HISTORY_PATH = os.path.join(os.path.dirname(__file__), 'history')

TRIVIA_PATH = os.path.join(os.path.dirname(__file__), 'trivial')
INTELLECTUAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoIntelectual.triv')
PHISICAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoFisico.triv')
SOCIAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoSocial.triv')

# TRIVIA FUNCTIONS

def getRandomQuestion(file_name):

    with open(file_name, encoding="utf8") as f:
        lines = f.readlines()
    
    questionNumber = random.randint(0,len(lines) - 1)
    
    return lines[questionNumber]

def triviaQuestionsOffice():
    option = None

    menuHeader = 'OFICINA DE PREGUNTAS TORMENTOSAS:\n[Elige una de las tres opciones para recibir una pregunta aleatoria]\n'
    menuOptions = ['Tormento Social', 'Tormento Físico', 'Tormento Intelectual', 'Salir']

    while option != 'Salir':
        option = menu(menuHeader, menuOptions)

        if option != 'Salir':
            option2 = None

            while option2 != 'Salir':
                question = 'N/A'
                questionType = 'N/A'

                if option == menuOptions[0]:
                    question = getRandomQuestion(SOCIAL_TORMENT_PATH)
                    questionType = menuOptions[0]

                elif option == menuOptions[1]:
                    question = getRandomQuestion(PHISICAL_TORMENT_PATH)
                    questionType = menuOptions[1]

                elif option == menuOptions[2]:
                    question = getRandomQuestion(INTELLECTUAL_TORMENT_PATH)
                    questionType = menuOptions[2]

                questionHeader = ' * ' + questionType.upper() + ' * \n\n  ' + question + '\n'
                questionOptions = ['Otra pregunta de ' + questionType, 'Salir']

                option2 = menu(questionHeader, questionOptions)

# MONEY LAUNDERING FUNCTIONS

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

# TURN/HISTORY/SAVES FUNCTIONS

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
        ret += str(values['ring_number']) + '. ' + values['name'] + '\n\n'
        ret += '   - Sentido: ' + values['direction'] + '\n'
        ret += '   - Distancia: ' + str(values['distance']) + '\n'
        ret +=  '\n\n'

    return ret

def saveGame(history):
    filename = datetime.now().strftime('%d%m%Y_%H%M%S') + '.his'
    
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
    parameters = loadYaml(os.path.join(os.path.dirname(__file__), 'parameters.yaml'))
    
    history = hist

    actualTurn = len(history) + 1
    latestTurn = len(history) + 1
    history.append(generateTurn(latestTurn, parameters))

    option = None
    
    while option != 'Salir':

        # DISPLAY TURN AND CHOOSE OPTION
        if actualTurn == latestTurn:
            options = ['Nuevo turno', 'Turno anterior', 'Uso de item', 'Oficina de cambio de moneda', 'Preguntas tormentosas', 'Salir']
        else:
            options = ['Turno siguiente', 'Turno anterior', 'Ir al turno más reciente', 'Salir']

        option = menu(turnToString(history[actualTurn - 1], isLatestTurn=(latestTurn == actualTurn)), options)

        # HANDLE OPTIONS
        if option == 'Nuevo turno':
            latestTurn += 1
            actualTurn = latestTurn
            history.append(generateTurn(latestTurn, parameters))

        elif option == 'Turno anterior':
            if actualTurn != 1:
                actualTurn -= 1

        elif option == 'Uso de item':
            pass

        elif option == 'Oficina de cambio de moneda':
            moneyExchangeOffice()

        elif option == 'Turno siguiente':
            actualTurn += 1

        elif option == 'Ir al turno más reciente':
            actualTurn = latestTurn

        elif option == 'Preguntas tormentosas':
            triviaQuestionsOffice()

        elif option == 'Salir':
            confirm = menu('¿Seguro que quieres salir?\n', ['Si', 'No'])

            if confirm == 'No':
                option = None
            else:
                wantSave = menu('¿Quieres guardar la partida?\n', ['Si', 'No'])

                if wantSave == 'Si':
                    saveGame(history)
