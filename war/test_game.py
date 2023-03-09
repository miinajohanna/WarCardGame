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
        instance = game.self()
        cls = game.self
        self.assertIsInstance(instance, cls)

    def test_war(self):
        """Test war method functionality."""
        check_list = [
            self.hand1[0],
            self.hand2[0],
            self.hand1[1],
            self.hand2[1],
            self.hand1[2],
            self.hand2[2],
        ]
        game.self.war(self.empty_list, self.hand1, self.hand2)
        self.assertListEqual(self.empty_list, check_list)
        self.assertEqual(self.empty_list, check_list)
        self.assertIn(1, self.empty_list)
        self.assertIn(2, self.empty_list)
        self.assertIn(5, self.empty_list)

    def test_war_type(self):
        """Test that the function is appending elements to a list."""
        game.self.war(self.empty_list, self.hand1, self.hand2)
        self.assertIs(type(self.empty_list), list)

    def test_war_value_type(self):
        """Test that the type used is list and int."""
        check_list = [
            self.hand1[0],
            self.hand2[0],
            self.hand1[1],
            self.hand2[1],
            self.hand1[2],
            self.hand2[2],
        ]
        self.assertIs(type(check_list), list)
        self.assertIs(type(check_list[0]), int)

    def test_add_won_cards_to_deck(self):
        """Test the elements that are appended to a list."""
        card_one = (3, "H")
        card_two = (12, "S")
        war_card = [(11, "C"), (5, "D"), (3, "C")]
        game.self.add_won_cards_to_deck(
            self.empty_list, card_one, card_two, war_card)

        equal_list = [(3, "H"), (12, "S"), (11, "C"), (5, "D"), (3, "C")]
        self.assertEqual(equal_list, self.empty_list)
        self.assertIn(card_one, self.empty_list)
        self.assertIn(card_two, self.empty_list)
        self.assertEqual(war_card, [])

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
        create_deck = game.self.create_deck()
        self.assertEqual(52, len(create_deck))
        self.assertTupleEqual((2, "Hearts"), create_deck[0])
        self.assertTupleEqual((3, "Hearts"), create_deck[1])
        self.assertTupleEqual((4, "Hearts"), create_deck[2])

    def test_game_create_deck_type(self):
        """Test the card deck type is list."""
        create_deck = game.self.create_deck()
        self.assertIs(type(create_deck), list)

    def test_game_create_deck_card_type(self):
        """Test the card deck elements are tuples."""
        create_deck = game.self.create_deck()
        self.assertIs(type(create_deck[0]), tuple)

    def test_create_hands(self):
        """Test that the hands are even in length."""
        deck = game.self.create_deck()
        hand_one, hand_two = game.self.create_hands(deck)
        self.assertEqual(26, len(hand_one))
        self.assertEqual(26, len(hand_two))

    def test_create_hands_type(self):
        """Test the hand type is list of tuples."""
        deck = game.self.create_deck()
        hand_one, hand_two = game.self.create_hands(deck)
        self.assertIs(type(hand_one), list)
        self.assertIs(type(hand_two), list)
        self.assertIs(type(hand_one[0]), tuple)
        self.assertIs(type(hand_two[0]), tuple)


if __name__ == "__main__":
    unittest.main()
