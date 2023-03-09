import unittest
import player


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def setUp(self):
        self.player = player.Player("Bob")
        self.display_name = player.Player().displayName()

    def test_player(self):
        instance = player.Player()
        cls = player.Player
        self.assertIsInstance(instance, cls)
        self.assertEqual("Computer", instance.name)

    def test_player_type(self):
        self.assertIs(type(self.player), player.Player)

    def test_player_name_type(self):
        self.assertIs(type(self.player.name), str)

    def test_player_name_type_is_not_int(self):
        self.assertIsNot(type(self.player.name), int)

    def test_player_name_type_is_not_object(self):
        self.assertIsNot(type(self.player.name), object)

    def test_player_name_type_is_not_list(self):
        self.assertIsNot(type(self.player.name), list)

    def test_player_change_name(self):
        self.assertEqual("Bob", self.player.name)

        self.player.changeName("Jack")
        self.assertEqual("Jack", self.player.name)

    def test_player_display_name(self):
        self.display_name
        self.assertEqual("Computer", self.display_name)

    def test_player_display_name_type(self):
        self.assertIs(type(self.display_name), str)

    def test_player_display_name_type_is_not_int(self):
        self.assertIsNot(type(self.display_name), int)


if __name__ == "__main__":
    unittest.main()
