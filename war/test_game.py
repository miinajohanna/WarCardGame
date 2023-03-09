"""Unit testing."""

import unittest
import game


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def setUp(self):
        self.empty_list = []
        self.hand1 = [1, 2, 3, 4]
        self.hand2 = [5, 6, 7, 8]

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        instance = game.Game()
        cls = game.Game
        self.assertIsInstance(instance, cls)

    def test_war(self):
        """Test war method"""
        check_list = [
            self.hand1[0],
            self.hand2[0],
            self.hand1[1],
            self.hand2[1],
            self.hand1[2],
            self.hand2[2],
        ]
        game.Game.war(self.empty_list, self.hand1, self.hand2)
        self.assertListEqual(self.empty_list, check_list)
        self.assertEqual(self.empty_list, check_list)
        self.assertIn(1, self.empty_list)
        self.assertIn(2, self.empty_list)
        self.assertIn(5, self.empty_list)

    def test_war_type(self):
        game.Game.war(self.empty_list, self.hand1, self.hand2)
        self.assertIs(type(self.empty_list), list)

    def test_war_value_type(self):
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
        cardOne = (3, "H")
        cardTwo = (12, "S")
        warCards = [(11, "C"), (5, "D"), (3, "C")]
        game.Game.addWonCardsToDeck(self.empty_list, cardOne, cardTwo, warCards)

        equal_list = [(3, "H"), (12, "S"), (11, "C"), (5, "D"), (3, "C")]
        self.assertEqual(equal_list, self.empty_list)
        self.assertIn(cardOne, self.empty_list)
        self.assertIn(cardTwo, self.empty_list)
        self.assertEqual(warCards, [])

    def test_add_won_cards_to_deck_type(self):
        cardOne = (3, "H")
        cardTwo = (12, "S")
        warCards = [(11, "C"), (5, "D"), (3, "C")]
        self.assertIs(type(cardOne), tuple)
        self.assertIs(type(cardTwo), tuple)
        self.assertIs(type(warCards), list)
        self.assertIs(type(warCards[0]), tuple)

    def test_game_create_deck(self):
        cd = game.Game.createDeck()
        self.assertEqual(52, len(cd))
        self.assertTupleEqual((2, "Hearts"), cd[0])
        self.assertTupleEqual((3, "Hearts"), cd[1])
        self.assertTupleEqual((4, "Hearts"), cd[2])

    def test_game_create_deck_type(self):
        cd = game.Game.createDeck()
        self.assertIs(type(cd), list)

    def test_game_create_deck_card_type(self):
        cd = game.Game.createDeck()
        self.assertIs(type(cd[0]), tuple)

    def test_create_hands(self):
        deck = game.Game.createDeck()
        h1, h2 = game.Game.createHands(deck)
        self.assertEqual(26, len(h1))
        self.assertEqual(26, len(h2))

    def test_create_hands_type(self):
        deck = game.Game.createDeck()
        h1, h2 = game.Game.createHands(deck)
        self.assertIs(type(h1), list)
        self.assertIs(type(h2), list)
        self.assertIs(type(h1[0]), tuple)
        self.assertIs(type(h2[0]), tuple)


if __name__ == "__main__":
    unittest.main()
