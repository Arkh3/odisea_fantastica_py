from utils.utils import menu, flush_input
from game_resources.game import startGame, getSavedGamesList, getSavedGame
import traceback

def main():
    try:
        mainHeader = "ODISEA FANTÁSTICA\n\n\n" 
        options = ['Empezar nueva partida', 'Cargar partida', 'Salir']

        exit = False
        option = None

        while not exit:
            option = menu(mainHeader + " Menú Principal:\n", options, markedOption=option, confirmOptions='Salir')

            if option == 'Empezar nueva partida':
                startGame([])
            
            elif option == 'Cargar partida':
                savedGames = getSavedGamesList()
                option2 = menu(mainHeader + " Partidas guardadas\n", savedGames + ['Volver al menú'])

                if option2 != 'Volver al menú':
                    loadedGame = getSavedGame(option2)
                    startGame(loadedGame)
                
            elif option == "Salir":
                exit = True
    except:
        print("\n¡OOPS! ALGO HA FALLADO (parece que no se hacer mi trabajo)\nImprimiendo traceback: \n")
        print(traceback.format_exc())

    flush_input()

if __name__ == '__main__':
    main()