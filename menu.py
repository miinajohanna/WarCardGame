
class Menu:
    def printMenu():    
        print('\n   M E N U   \n')
        print('1. PLAY GAME')
        print('2. Game Rules')
        print('3. Change name')
        print('4. Show scores')
        print('5. Exit game\n')

    def printRules():
        print('\n G A M E   R U L E S\n')
        print('\nEach player turns up a card at the same time. The player with the higher card')
        print('takes both cards and puts them face down on the bottom of his stack.')
        print('\nIf the cards are the same rank, it is WAR. Each player sets three cards') 
        print('face down and a fourth card face up on the game board.')
        print('\nThe player with the higher top card wins both piles.') 
        print('If the top cards are again the same rank, WAR repeats.')
        print('\nThe game ends when one player has won all the cards.')
        print('If a player runs out of cards during WAR, the other player wins.\n')
