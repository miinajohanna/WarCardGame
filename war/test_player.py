"""Unittests for the Player class."""

import unittest
import player


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def setUp(self):
        """Set up the test environment."""
        self.player = player.Player("Bob")
        self.display_name = player.Player().display_name()

    def test_player(self):
        """Testing the Player instance."""
        instance = player.Player()
        cls = player.Player
        self.assertIsInstance(instance, cls)
        self.assertEqual("Computer", instance.name)

    def test_player_type(self):
        """Testing Player type."""
        self.assertIs(type(self.player), player.Player)

    def test_player_name_type(self):
        """Testing the player name is a string."""
        self.assertIs(type(self.player.name), str)

    def test_player_name_type_is_not_int(self):
        """Ensuring Player name type is not int."""
        self.assertIsNot(type(self.player.name), int)

    def test_player_name_type_is_not_object(self):
        """Ensuring the Player name is not an object."""
        self.assertIsNot(type(self.player.name), object)

    def test_player_name_type_is_not_list(self):
        """Ensuring the Player name is not a list."""
        self.assertIsNot(type(self.player.name), list)

    def test_player_change_name(self):
        """Testing the name changing function."""
        self.assertEqual("Bob", self.player.name)

        self.player.change_name("Jack")
        self.assertEqual("Jack", self.player.name)

    def test_player_display_name(self):
        """Testing the name displaying method."""
        self.assertEqual("Computer", self.display_name)

    def test_player_display_name_type(self):
        """Testing that the display name method returns a string."""
        self.assertIs(type(self.display_name), str)

    def test_player_display_name_type_is_not_int(self):
        """Ensuring that the Player name is not displayed as an int."""
        self.assertIsNot(type(self.display_name), int)


if __name__ == "__main__":
    unittest.main()
