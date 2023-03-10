"""Compare cards, highest card wins."""

import random

class Game:
    """War card game."""

    war_cards = []
    card_one = ()
    card_two = ()
    space_between = ' ' * 10

    def __init__(self):
        """Initialize the object."""
        random.seed()

    def create_deck(self):
        """Create the card deck."""
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.deck = [(rank, suit) for rank in range(2, 15) for suit in suits]
        return self.deck
    
    def create_hands(self):
        """Create hands for each player."""
        self.hand_one = random.sample(self.deck, k=26)
        self.hand_two = [i for i in self.deck if i not in self.hand_one]
        random.shuffle(self.hand_two)
        return self.hand_one, self.hand_two

    def display_cards(self):
        """Display the compared cards."""
        print(f"\n -------- {self.space_between} -------- ")
        print(f"|{self.card_one[0]:<8}|" + " " * 10 + f"|{self.card_two[0]:<8}|")
        print(f"|        |{self.space_between}|        |")
        print(f"|{self.card_one[1]:^8}|{self.space_between}|{self.card_two[1]:^8}|")
        print(f"|        |{self.space_between}|        |")
        print(f"|{self.card_one[0]:>8}|{self.space_between}|{self.card_two[0]:>8}|")
        print(f" -------- {self.space_between} --------\n")
    
    def conceal_cards(self):
        """Display cards face down."""
        print("\n --------            --------")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print("| * * * *|          | * * * *|")
        print("|* * * * |          |* * * * |")
        print(" --------            --------\n")

    def print_rules(self):
        """Display the rules."""
        msg = ("\n\n G A M E   R U L E S"
            "\nEach player turns up a card at the same time. The player with the\n"
            "higher card adds both cards to the bottom of their stack.\n"
            "\nIf the cards are the same rank, it is WAR. Each player sets\n"
            "three cards face down and a fourth card face up on the board.\n"
            "\nThe player with the higher top card wins both piles.\n"
            "If the top cards are again the same rank, WAR repeats.\n"
            "The game ends when one player has won all the cards.\n"
            "\nIf a player runs out of cards during WAR, the other player wins.\n\n"
            )
        print(msg)
    
    def pop_cards(self):
        """Popping cards off hands to compare them."""
        self.card_one = self.hand_one.pop(0)
        self.card_two = self.hand_two.pop(0)
        return self.card_one, self.card_two
    
    def compare_cards(self):
        """Comparing two cards."""
        if self.card_one[0] > self.card_two[0]:
            return 1
        elif self.card_one[0] < self.card_two[0]:
            return 2
        else:
            return 0
    
    def war(self):
        """Appending concealed cards to war cards list."""
        if len(self.hand_one) > 0 and len(self.hand_two) > 0:
            self.war_cards.append(self.hand_one.pop(0))
            self.war_cards.append(self.hand_two.pop(0))
        return self.war_cards

    def add_cards_to_deck(self, hand):
        """Add cards to winner's hand (either hand one or two)."""
        hand.append(self.card_one)
        hand.append(self.card_two)
        hand.extend(self.war_cards)
        self.war_cards.clear()
        return hand, self.war_cards
    
    def win_check(self):
        """Checking if either player has reached 52 or 0 cards."""
        if len(self.hand_one) == 0:
            return 2
        elif len(self.hand_two) == 0: 
            return 1

    def display_cards_left(self, player1, player2):
        """Displays who won the round and how many cards are left."""
        print(f"\n{len(self.hand_one):<3} cards left for {player1}")
        print(f"{len(self.hand_two):<3} cards left for {player2}")
    
