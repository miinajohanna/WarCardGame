"""Unit testing."""

import unittest
import game


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def setUp(self):
        """Set up the testing environment."""
        self.empty_list = []
        self.hand1 = [1, 2, 3, 4]
        self.hand2 = [5, 6, 7, 8]

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        instance = game.Game()
        cls = game.Game
        self.assertIsInstance(instance, cls)

    def test_add_won_cards_to_deck_type(self):
        """Ensure that the elements are type tuple in type list."""
        card_one = (3, "H")
        card_two = (12, "S")
        war_cards = [(11, "C"), (5, "D"), (3, "C")]
        self.assertIs(type(card_one), tuple)
        self.assertIs(type(card_two), tuple)
        self.assertIs(type(war_cards), list)
        self.assertIs(type(war_cards[0]), tuple)

    def test_game_create_deck(self):
        """Test the card deck length and elements."""
        create_deck = game.Game().create_deck()
        self.assertEqual(52, len(create_deck))
        self.assertTupleEqual((2, "Hearts"), create_deck[0])

    def test_game_create_deck_type(self):
        """Test the card deck type is list."""
        create_deck = game.Game().create_deck()
        self.assertIs(type(create_deck), list)

    def test_game_create_deck_card_type(self):
        """Test the card deck elements are tuples."""
        create_deck = game.Game().create_deck()
        self.assertIs(type(create_deck[0]), tuple)

    def test_pop_cards(self):
        """Test the pop function."""
        self.assertIs(type(game.Game.card_one), tuple)

    def test_war_cards_type(self):
        """Test the functionality of the win check."""
        self.assertIs(type(game.Game.war_cards), list)


if __name__ == "__main__":
    unittest.main()
