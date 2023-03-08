
class Player:
    def __init__(self, name = 'Computer', score = 0):
        self.name = name
        self.score = score
    
    def changeName(self, newName):
        self.name = newName

    def displayName(self):
        return self.name
    
    def updateScore(self, newScore = 1):
        self.score += newScore

    def displayScore(self):
        return self.score

    def __repr__(self):
        return self.name
