import os
from utils.utils import menu, flush_input, captureKeys

OFFICE_SIGN = 'OFICINA DE GESTIÓN DE ITEMS:'

# Gets the items that expired on the newest turn
def getExpiredItems(history):

    ret = []

    latestTurn = len(history)

    for turn in history:
        turnNumber = turn['number']

        for item in turn['items_used']:
            if turnNumber + item["turnDuration"] == latestTurn:
                ret.append(item)

    return ret


def showExpiredItems(history):
    expiredItems = getExpiredItems(history)

    if len(expiredItems) != 0:
        os.system('cls')
        print('LOS SIGUIENTES ITEMS DEJAN DE TENER EFECTO:\n')

        for item in expiredItems:

            print(itemToString(item))
            print(" ==========================================\n")

        print("Presiona [ENTER] para continuar...")
        captureKeys(['enter'])
        

# Gets the info of all the items which are not expired
def getActiveItems(history):
    ret = []

    latestTurn = len(history)

    for turn in history:
        turnNumber = turn['number']

        for item in turn['items_used']:
            if turnNumber + item["turnDuration"] > latestTurn:
                ret.append(item)

    return ret


def activeItemsToString(history):

    ret = " ACTUALMENTE NO HAY NINGÚN OBJETO ACTIVO \n\n"
    activeItems = getActiveItems(history)

    if len(activeItems) != 0:

        ret = " OBJETOS ACTUALMENTE ACTIVOS: \n\n"

        for item in activeItems:
            ret += itemToString(item)
            ret += " =====================================\n"

    return ret


def itemToString(item):
    return " - Nombre: " + item["item"] + "\n - Propietario: " + item["owner"] + "\n - Turno de uso: " + str(item["turn_used"]) + "\n - Duración: " + str(item["turnDuration"]) + "\n"


def createItem(turn_number):

    item = None
    exit = False
    
    while not exit:

        item = {"item": "",
            "owner": "",
            "turnDuration": -1,
            "turn_used": turn_number
            }

        os.system('cls')
        flush_input()

        print(OFFICE_SIGN + "\n")
        # Get the name
        item["item"] = input('(1 de 3) Nombre del item: ')

        # Get the owner
        item["owner"] = input('(2 de 3) Propietario del item: ')

        # Get the turnDuration
        rightValue = False
        
        while not rightValue:
            print('\n[El valor insertado debe ser un número natural]')
            activeTurns = input('(3 de 3) Cuántos turnos dura el item: ')

            try:
                item["turnDuration"] = int(activeTurns)

                if item["turnDuration"] < 0:
                    raise ValueError

                rightValue = True
            except ValueError:
                pass
        
        questionHeader = OFFICE_SIGN + '\n\n Item:\n' + itemToString(item) + '\n'
        questionOptions = ['Guardar item', 'Rehacer el item', 'Salir sin guardar']

        exit2 = False

        while not exit2:
            option = menu(questionHeader, questionOptions)

            if option == 'Guardar item':
                confirm = menu(questionHeader + " ¿Seguro que quieres guardar el objeto?\n", ['Si', 'No'])

                if confirm == 'Si':
                    exit = True
                    exit2 = True

            elif option == 'Rehacer el item':
                exit2 = True

            elif option == 'Salir sin guardar':
                exit = True
                exit2 = True
                item = None

    return item


def addItem(history, turn=None):
    if turn is None or turn < 0 or turn >= len(history):
        turn = len(history) - 1
    
    item = createItem(turn + 1)

    if item is not None:
        history[turn]['items_used'].append(item)

    return history


def itemManagementOffice(history):

    option = None

    while option != 'Salir':
        header = OFFICE_SIGN  + '\n\n' + activeItemsToString(history)
        option = menu(header, ['Añadir item', 'Salir'], markedOption=option)

        if option == 'Añadir item':
            addItem(history)


    return history