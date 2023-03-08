from deck import *
from cardHand import *
from menu import *
from game import *

class Main:
    print('\n-------- Welcome to a game of W A R! --------\n')
    invalid = True
    while invalid:
            gameMode = input('\nSingle-player or two-player game mode? (press 1 or 2): ')
            if gameMode == '1' or gameMode == '2':
                invalid = False
            else:
                print('Only 1 or 2 allowed! Try again!')

    player1 = Player(input('\nPlease enter a name for player 1: '))
    if gameMode == '1':
        player2 = Player()
    elif gameMode == '2':
        player2 = Player(input('\nPlease enter a name for player 2: '))

    cond = True
    while cond:
        Menu.printMenu()
        option = input('\nEnter an option: ')
        if option == '1':
            deck = Deck.createDeck()
            handOne, handTwo = CardHand.createHands(deck)
            Game.runGame(handOne, handTwo, player1, player2)
        elif option == '2':
            Menu.printRules()
        elif option == '3':
            player1.changeName(input(f'\n{player1}, enter new name: '))
            if gameMode == '2':
                player2.changeName(input(f'\n{player2} enter new name: '))
        elif option == '4':
            print(f'{player1.displayName():<10}:{player1.displayScore():>5}')
            print(f'{player2.displayName():<10}:{player2.displayScore():>5}')
            # should these be stored into a file?
        elif option == '5':
            print('\n       B            Y              E\n')
            cond = False
        else:
            print('\nOnly choices between 1-4 allowed! Try again!\n')


if __name__ == '__main__':
    Main()
