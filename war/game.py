from player import *
import random


class Game:
    """Class for the War Game"""

    def printMenu():
        """Displays the game menu"""
        print("\n   M E N U   \n")
        print("1. PLAY GAME")
        print("2. Game Rules")
        print("3. Change name")
        print("4. Exit game\n")

    def printRules():
        """Displays the rules"""
        print("\n G A M E   R U L E S\n")
        print(
            "\nEach player turns up a card at the same time. The player with the higher card"
        )
        print("takes both cards and puts them face down on the bottom of his stack.")
        print(
            "\nIf the cards are the same rank, it is WAR. Each player sets three cards"
        )
        print("face down and a fourth card face up on the game board.")
        print("\nThe player with the higher top card wins both piles.")
        print("If the top cards are again the same rank, WAR repeats.")
        print("\nThe game ends when one player has won all the cards.")
        print("If a player runs out of cards during WAR, the other player wins.\n")

    def createDeck():
        """Creates the card deck"""
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        deck = []
        for suit in suits:
            for card in range(13):
                deck.append((card + 2, suit))
        return deck

    def createHands(deck):
        """Creates hands for each player"""
        handOne = random.sample(deck, k=26)
        handTwo = [i for i in deck if i not in handOne]
        return handOne, handTwo

    def printCardsFaceUp(cardOne, cardTwo, player1, player2):
        """Displays cards"""
        print(f"\n {player1}       vs.      {player2} ")
        print(" -------- " + " " * 10 + " -------- ")
        print(f"|{cardOne[0]:<8}|" + " " * 10 + f"|{cardTwo[0]:<8}|")
        print("|        |" + " " * 10 + "|        |")
        print(f"|{cardOne[1]:^8}|" + " " * 10 + f"|{cardTwo[1]:^8}|")
        print("|        |" + " " * 10 + "|        |")
        print(f"|{cardOne[0]:>8}|" + " " * 10 + f"|{cardTwo[0]:>8}|")
        print(" -------- " + " " * 10 + " -------- \n")

    def printCardFaceDown():
        """Displays cards face down"""
        print("\n --------            --------")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print(" --------            --------\n")

    def war(warCards, handOne, handTwo):
        """Plays cards during Tie breaker"""
        i = 0
        while i < 3:
            Game.printCardFaceDown()
            warCards.append(handOne.pop(0))
            warCards.append(handTwo.pop(0))
            i += 1

    def winCheck(handOne, handTwo, player1, player2):
        """Display's the winner"""
        if handOne == []:
            print(f"\n{player2} WINS!\n")
        elif handTwo == []:
            print(f"\n{player1} WINS!\n")

    def addWonCardsToDeck(hand, cardOne, cardTwo, warCards):
        """Adds cards to winner's hand"""
        hand += [cardOne, cardTwo] + warCards
        warCards.clear()

    def runGame(handOne, handTwo, player1, player2):
        """Game loop"""
        warCards = []
        while len(handOne) > 0 and len(handTwo) > 0:
            option = input("\nEnter to set down a card face up! (cheat or menu) ")
            print()
            if option == "cheat":
                Game.cheat(handOne, handTwo, player1, player2)
                break
            elif option == "menu":
                break

            cardOne = handOne.pop(0)  # Playing hand for player one
            cardTwo = handTwo.pop(0)  # Playing hand for player two
            Game.printCardsFaceUp(cardOne, cardTwo, player1, player2)

            if cardOne[0] > cardTwo[0]:
                Game.addWonCardsToDeck(handOne, cardOne, cardTwo, warCards)
                print(
                    f"\n{player1} won the cards!\n{len(handOne):<3} cards left for {player1}\n{len(handTwo):<3} cards left for {player2}"
                )
            elif cardOne[0] < cardTwo[0]:
                Game.addWonCardsToDeck(handTwo, cardOne, cardTwo, warCards)
                print(
                    f"\n{player2} won the cards!\n{len(handOne):<3} cards left for {player1}\n{len(handTwo):<3} cards left for {player2}"
                )
            else:
                print("\n          W A R!\n")
                warCards.append(cardOne)
                warCards.append(cardTwo)
                Game.war(warCards, handOne, handTwo)

            Game.winCheck(handOne, handTwo, player1, player2)

    def cheat(handOne, handTwo, player1, player2):
        """Runs the game until completion"""
        warCards = []
        while len(handOne) > 0 and len(handTwo) > 0:
            cardOne = handOne.pop(0)
            cardTwo = handTwo.pop(0)
            print(
                f"\nComparing {cardOne[0]} of {cardOne[1]} and {cardTwo[0]} of {cardTwo[1]}\n"
            )
            if cardOne[0] > cardTwo[0]:
                Game.addWonCardsToDeck(handOne, cardOne, cardTwo, warCards)
                print(
                    f"{len(handOne):<3} cards left for {player1}\n{len(handTwo):<3} cards left for {player2}"
                )
            elif cardOne[0] < cardTwo[0]:
                Game.addWonCardsToDeck(handTwo, cardOne, cardTwo, warCards)
                print(
                    f"{len(handOne):<3} cards left for {player1}\n{len(handTwo):<3} cards left for {player2}"
                )
            else:
                print("W A R")
                warCards.append(cardOne)
                warCards.append(cardTwo)
                i = 0
                while i < 3:
                    print(f"War cards {i}")
                    if len(handOne) > 0 and len(handTwo) > 0:
                        warCards.append(handOne.pop(0))
                        warCards.append(handTwo.pop(0))
                    i += 1

            Game.winCheck(handOne, handTwo, player1, player2)

    def game():
        """Game Menu"""
        print("\n-------- Welcome to a game of W A R! --------\n")
        invalid = True
        while invalid:
            gameMode = input(
                "\nSingle-player or two-player game mode? (press 1 or 2): "
            )
            if gameMode == "1" or gameMode == "2":
                invalid = False
            else:
                print("Only 1 or 2 allowed! Try again!")

        player1 = Player(input("\nPlease enter a name for player 1: "))
        if gameMode == "1":
            player2 = Player()
        elif gameMode == "2":
            player2 = Player(input("\nPlease enter a name for player 2: "))

        cond = True
        while cond:
            Game.printMenu()
            option = input("\nEnter an option: ")
            if option == "1":
                deck = Game.createDeck()
                handOne, handTwo = Game.createHands(deck)
                Game.runGame(handOne, handTwo, player1, player2)
            elif option == "2":
                Game.printRules()
            elif option == "3":
                player1.changeName(input(f"\n{player1}, enter new name: "))
                if gameMode == "2":
                    player2.changeName(input(f"\n{player2} enter new name: "))
            elif option == "4":
                print("\n       B            Y              E\n")
                cond = False
            else:
                print("\nOnly choices between 1-4 allowed! Try again!\n")
