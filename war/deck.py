class Deck:
    def createDeck():
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        deck = []
        for suit in suits:
            for card in range(13):
                deck.append((card + 2, suit))
        return deck
