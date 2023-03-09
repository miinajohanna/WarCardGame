class Player:
    """The class of a player."""

    def __init__(self, name="Computer"):
        """Name of player."""
        self.name = name

    def changeName(self, newName):
        """Set new name."""
        self.name = newName

    def displayName(self):
        """Get name."""
        return self.name

    def __repr__(self):
        """Return string."""
        return self.name
