import os
import random
from utils.utils import menu

TRIVIA_PATH = os.path.join(os.path.dirname(__file__), 'trivial')

INTELLECTUAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoIntelectual.triv')
PHISICAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoFisico.triv')
SOCIAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoSocial.triv')

OFFICE_SIGN = 'OFICINA DE PREGUNTAS TORMENTOSAS:'


def getRandomQuestion(file_name):

    with open(file_name, encoding="utf8") as f:
        lines = f.readlines()
    
    questionNumber = random.randint(0,len(lines) - 1)
    
    return lines[questionNumber]


def triviaQuestionsOffice():
    option = None

    menuHeader = OFFICE_SIGN + '\n[Elige una de las tres opciones para recibir una pregunta aleatoria]\n'
    menuOptions = ['Tormento Social', 'Tormento Físico', 'Tormento Intelectual', 'Salir']

    while option != 'Salir':
        option = menu(menuHeader, menuOptions, markedOption=option)

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