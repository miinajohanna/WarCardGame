import random

class CardHand:
    def createHands(deck):
        handOne = random.sample(deck, k=26)
        handTwo = [i for i in deck if i not in handOne]
        return handOne, handTwo
