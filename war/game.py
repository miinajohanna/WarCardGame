from player import *


class Game:
    def printCardsFaceUp(cardOne, cardTwo, player1, player2):
        print(f"\n {player1}       vs.      {player2} ")
        print(" -------- " + " " * 10 + " -------- ")
        print(f"|{cardOne[0]:<8}|" + " " * 10 + f"|{cardTwo[0]:<8}|")
        print("|        |" + " " * 10 + "|        |")
        print(f"|{cardOne[1]:^8}|" + " " * 10 + f"|{cardTwo[1]:^8}|")
        print("|        |" + " " * 10 + "|        |")
        print(f"|{cardOne[0]:>8}|" + " " * 10 + f"|{cardTwo[0]:>8}|")
        print(" -------- " + " " * 10 + " -------- \n")

    def printCardFaceDown():
        print("\n --------            --------")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print(" --------            --------\n")

    def war(warCards, handOne, handTwo):
        i = 0
        while i < 3:
            input(f"\nSet down cards face down {i + 1}")
            Game.printCardFaceDown()
            warCards.append(handOne.pop(0))
            warCards.append(handTwo.pop(0))
            i += 1

    def winCheck(handOne, handTwo, player1, player2):
        if handOne == []:
            print(f"\n{player2} WINS!\n")
            return 2
        elif handTwo == []:
            print(f"\n{player1} WINS!\n")
            return 1

    def addWonCardsToDeck(hand, cardOne, cardTwo, warCards):
        hand.append(cardOne)
        hand.append(cardTwo)
        hand.extend(warCards)
        warCards.clear()

    def runGame(handOne, handTwo, player1, player2):
        warCards = []
        while len(handOne) > 0 and len(handTwo) > 0:
            option = input("\nEnter to set down a card face up! (cheat or menu) ")
            print()
            if option == "cheat":
                winner = Game.cheat(handOne, handTwo, player1, player2)
                break
            elif option == "menu":
                break

            cardOne = handOne.pop(0)
            cardTwo = handTwo.pop(0)
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


# adjust for single-player (no enters pressed for player two)
# fix cheat maybe add prints that show that something is happening
