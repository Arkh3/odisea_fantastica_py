import os
import random
from utils.utils import menu, loadYaml

TRIVIA_PATH = os.path.join(os.path.dirname(__file__), 'trivial')

INTELLECTUAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoIntelectual.yaml')
PHISICAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoFisico.yaml')
SOCIAL_TORMENT_PATH = os.path.join(TRIVIA_PATH, 'tormentoSocial.yaml')

OFFICE_SIGN = 'OFICINA DE PREGUNTAS TORMENTOSAS:'

def getRandomQuestion(file_name):

    questions = loadYaml(file_name)
    questionNumber = random.randint(0,len(questions) - 1)
    
    return questions[questionNumber]


def triviaQuestionsOffice():
    option = None
    option2 = None

    menuHeader = OFFICE_SIGN + '\n[Elige una de las tres opciones para recibir una pregunta aleatoria]\n'
    menuOptions = ['Tormento Social', 'Tormento Físico', 'Tormento Intelectual', 'Salir']

    option = menu(menuHeader, menuOptions, markedOption=option)
            
    while option != 'Salir':
        exit = False

        while not exit:
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

            questionHeader = ' * ' + questionType.upper() + ' * \n\n  ' + question['question'] + '\n'

            if 'answer' not in question:
                questionOptions = ['Otra pregunta de ' + questionType, 'Salir']
            else:
                questionOptions = ['Otra pregunta de ' + questionType, 'Ver respuesta', 'Salir']

            option2 = menu(questionHeader, questionOptions)

            if option2 == 'Ver respuesta':
                questionHeader2 = questionHeader + "Respuesta: " + question['answer']  + '\n'
                questionOptions2 = ['Otra pregunta de ' + questionType,  'Salir']

                option3 = menu(questionHeader2, questionOptions2)

                if option3 == 'Salir':
                    exit = True

            elif option2 == 'Salir':
                exit = True

        option = menu(menuHeader, menuOptions, markedOption=option)
