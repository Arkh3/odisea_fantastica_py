from utils.utils import menu, flush_input
from game_resources.game import startGame, getSavedGamesList, getSavedGame


def main():
    mainHeader = "ODISEA FANTÁSTICA\n\n\n" 
    options = ['Empezar nueva partida', 'Cargar partida', 'Salir']
    option = None

    exit = False
    while not exit:
        option = menu(mainHeader + " Menú Principal:\n", options, markedOption=option)

        if option == 'Empezar nueva partida':
            startGame()
        
        elif option == 'Cargar partida':
            
            savedGames = getSavedGamesList()
            option2 = menu(mainHeader + " Partidas guardadas\n", savedGames + ['Volver al menú'])

            if option2 != 'Volver al menú':
                loadedGame = getSavedGame(option2)
                startGame(loadedGame)
            
        elif option == "Salir":

            confirm = menu(mainHeader + " ¿Seguro que quieres salir?\n", ['Si', 'No'])

            if confirm == 'Si':
                exit = True
    
    flush_input()

if __name__ == '__main__':
    main()