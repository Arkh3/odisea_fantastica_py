from utils.utils import menu, flush_input
from game_resources.game import startGame, getSavedGamesList, getSavedGame


def main():
    options = ['Empezar nueva partida', 'Cargar partida', 'Salir']
    option = None

    while(option != 'Salir'):
        option = menu("ODISEA FANTÁSTICA\n\n\n Menú Principal:\n", options)

        if option == 'Empezar nueva partida':
            startGame()
        
        elif option == 'Cargar partida':
            
            savedGames = getSavedGamesList()
            option2 = menu("Partidas guardadas\n", savedGames + ['Volver al menú'])

            if option2 != 'Volver al menú':
                loadedGame = getSavedGame(option2)
                startGame(loadedGame)
            
        elif option == "Salir":

            confirm = menu("¿Seguro que quieres salir?\n", ['Si', 'No'])

            if confirm == 'No':
                option = None
    
    flush_input()

if __name__ == '__main__':
    main()