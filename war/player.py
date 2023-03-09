"""Contains the class Player."""


class Player:
    """The class of a player."""

    def __init__(self, name="Computer"):
        """Name of player."""
        self.name = name

    def change_name(self, new_name):
        """Set new name."""
        self.name = new_name

    def display_name(self):
        """Get name."""
        return self.name

    def __repr__(self):
        """Return string."""
        return self.name
