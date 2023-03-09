"""Game class."""

import random
import player


class Game:
    """Class for the War Game."""

    def __init__(self):
        pass

    def print_menu(self):
        """Display the game menu."""
        print("\n   M E N U   \n")
        print("1. PLAY GAME")
        print("2. Game Rules")
        print("3. Change name")
        print("4. Exit game\n")

    def print_rules(self):
        """Display the rules."""
        print("\n G A M E   R U L E S\n\n")
        print(
            "Each player turns up a card at the same time. The player with the"
        )
        print(
            "higher card adds both cards to the bottom of their stack.\n"
            )
        print(
            "If the cards are the same rank, it is WAR. Each player sets"
        )
        print(
            "three cards face down and a fourth card face up on the board.")
        print("\nThe player with the higher top card wins both piles.")
        print("If the top cards are again the same rank, WAR repeats.")
        print("\nThe game ends when one player has won all the cards.")
        print(
            "If a player runs out of cards during WAR, the other player wins."
            )

    def create_deck(self):
        """Create the card deck."""
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        deck = []
        for suit in suits:
            for card in range(13):
                deck.append((card + 2, suit))
        return deck

    def create_hands(self, deck):
        """Create hands for each player."""
        hand_one = random.sample(deck, k=26)
        hand_two = [i for i in deck if i not in hand_one]
        return hand_one, hand_two

    def print_cards_face_up(self, card_one, card_two, player1, player2):
        """Display the compared cards."""
        print(f"\n {player1}       vs.      {player2} ")
        print(" -------- " + " " * 10 + " -------- ")
        print(f"|{card_one[0]:<8}|" + " " * 10 + f"|{card_two[0]:<8}|")
        print("|        |" + " " * 10 + "|        |")
        print(f"|{card_one[1]:^8}|" + " " * 10 + f"|{card_two[1]:^8}|")
        print("|        |" + " " * 10 + "|        |")
        print(f"|{card_one[0]:>8}|" + " " * 10 + f"|{card_two[0]:>8}|")
        print(" -------- " + " " * 10 + " -------- \n")

    def print_card_face_down(self):
        """Display cards face down."""
        print("\n --------            --------")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print(" --------            --------\n")

    def war(self, war_cards, hand_one, hand_two):
        """Play cards during Tie breaker."""
        i = 0
        while i < 3:
            self.print_card_face_down()
            war_cards.append(hand_one.pop(0))
            war_cards.append(hand_two.pop(0))
            i += 1

    def win_check(self, hand_one, hand_two, player1, player2):
        """Display the winner."""
        if hand_one == []:
            print(f"\n{player2} WINS!\n")
        elif hand_two == []:
            print(f"\n{player1} WINS!\n")

    def add_won_cards_to_deck(self, hand, card_one, card_two, war_cards):
        """Add cards to winner's hand."""
        hand += [card_one, card_two] + war_cards
        war_cards.clear()

    def run_game(self, hand_one, hand_two, player1, player2):
        """Game loop."""
        war_cards = []
        while len(hand_one) > 0 and len(hand_two) > 0:
            option = input("\nPress Enter (menu or cheat) ")
            print()
            if option == "cheat":
                self.cheat(hand_one, hand_two, player1, player2)
                break
            if option == "menu":
                break

            card_one = hand_one.pop(0)  # Playing hand for player one
            card_two = hand_two.pop(0)  # Playing hand for player two
            self.print_cards_face_up(card_one, card_two, player1, player2)

            if card_one[0] > card_two[0]:
                self.add_won_cards_to_deck(
                    hand_one, card_one, card_two, war_cards)
                print(f"\n{player1} won the cards!\n")
                print(f"{len(hand_one):<3} cards left for {player1}\n")
                print(f"{len(hand_two):<3} cards left for {player2}")
            elif card_one[0] < card_two[0]:
                self.add_won_cards_to_deck(
                    hand_two, card_one, card_two, war_cards)
                print(f"\n{player2} won the cards!\n")
                print(f"{len(hand_one):<3} cards left for {player1}\n")
                print(f"{len(hand_two):<3} cards left for {player2}")
            else:
                print("\n          W A R!\n")
                war_cards.append(card_one)
                war_cards.append(card_two)
                self.war(war_cards, hand_one, hand_two)

            self.win_check(hand_one, hand_two, player1, player2)

    def cheat(self, hand_one, hand_two, player1, player2):
        """Run the game until completion."""
        war_cards = []
        while len(hand_one) > 0 and len(hand_two) > 0:
            card_one = hand_one.pop(0)
            card_two = hand_two.pop(0)
            print(
                f"\nComparing {str(card_one)} and {str(card_two)}\n"
            )
            if card_one[0] > card_two[0]:
                self.add_won_cards_to_deck(
                    hand_one, card_one, card_two, war_cards)
                print(f"{len(hand_one):<3} cards left for {player1}")
                print(f"\n{len(hand_two):<3} cards left for {player2}")
            elif card_one[0] < card_two[0]:
                self.add_won_cards_to_deck(
                    hand_two, card_one, card_two, war_cards)
                print(f"{len(hand_one):<3} cards left for {player1}")
                print(f"\n{len(hand_two):<3} cards left for {player2}")
            else:
                print("W A R")
                war_cards.append(card_one)
                war_cards.append(card_two)
                i = 0
                while i < 3:
                    print(f"War cards {i+1}")
                    if len(hand_one) > 0 and len(hand_two) > 0:
                        war_cards.append(hand_one.pop(0))
                        war_cards.append(hand_two.pop(0))
                    i += 1

            self.win_check(hand_one, hand_two, player1, player2)

    def game(self):
        """Game Menu."""
        invalid = True
        while invalid:
            game_mode = input(
                "\nSingle-player or two-player game mode? (press 1 or 2): "
            )
            if game_mode in ('1', '2'):
                invalid = False
            else:
                print("Only 1 or 2 allowed! Try again!")

        player1 = player.Player(input("\nPlease enter a name for player 1: "))
        if game_mode == "1":
            player2 = player.Player()
        elif game_mode == "2":
            player2 = player.Player(input(
                "\nPlease enter a name for player 2: "))

        cond = True
        while cond:
            self.print_menu()
            option = input("\nEnter an option: ")
            if option == "1":
                deck = self.create_deck()
                hand_one, hand_two = self.create_hands(deck)
                self.run_game(hand_one, hand_two, player1, player2)
            elif option == "2":
                self.print_rules()
            elif option == "3":
                player1.change_name(input(f"\n{player1}, enter new name: "))
                if game_mode == "2":
                    player2.change_name(input(f"\n{player2} enter new name: "))
            elif option == "4":
                print("\n       B            Y              E\n")
                cond = False
            else:
                print("\nOnly choices between 1-4 allowed! Try again!\n")
