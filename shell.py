"""Cmd module shell for the main program."""

import cmd
import game
import player

class Shell(cmd.Cmd):
    """Class that compares playing cards in a game of war card game."""

    intro = "Type help or ? to list commands.\n"
    prompt = "(war) "

    def __init__(self):
        """Initialize the game object."""
        super().__init__()
        self.game = game.Game()
        self.player1 = player.Player()
        self.player2 = player.Player()

    def do_name(self, arg):
        """Set a new name."""
        option = input('\nWhich name do you want to update? (1 or 2) ')
        if option == '1':
            self.player1.change_name(input('\nPlease enter the new name: '))
        if option == '2':
            self.player2.change_name(input('\nPlease enter the new name: '))

    def do_game(self, _):
        """Compare two cards, add won cards to deck."""
        self.game.create_deck()
        self.game.create_hands()
        while len(self.game.hand_one) > 0 and len(self.game.hand_two) > 0:
            self.game.pop_cards()
            option = input('\nPress enter to compare cards (exit/cheat) ')
            if option == 'cheat':
                self.do_cheat(_)
                break
            elif option == 'exit':
                self.do_exit(_)
                break
            else:
                print(f'\n{self.player1}      vs.      {self.player2}')
                self.game.display_cards()
            round_win = self.game.compare_cards()
            if round_win == 0:  # war
                print('\n       W A R !')
                self.game.war_cards.append(self.game.card_one)
                self.game.war_cards.append(self.game.card_two)
                for i in range(3):
                    self.game.war()
                    input('\nPress enter to put down three cards ')
                    self.game.conceal_cards()
            elif round_win == 1:  # player1 wins
                self.game.add_cards_to_deck(self.game.hand_one)
                print(f'\n{self.player2} wins the cards')
                self.game.display_cards_left(self.player1, self.player2)
            elif round_win == 2:  # player2 wins
                self.game.add_cards_to_deck(self.game.hand_two)
                print(f'\n{self.player2} wins the cards')
                self.game.display_cards_left(self.player1, self.player2)
            winner = self.game.win_check()
            if winner == '1':
                print(f'\n{self.player1} WINS!')
            elif winner == '2':
                print(f'\n{self.player2} WINS!')

    
    def do_cheat(self, _):
        """Cheat and get straight to the winner."""
        self.game.create_deck()
        self.game.create_hands()
        while len(self.game.hand_one) > 0 and len(self.game.hand_two) > 0:
            self.game.pop_cards()
            round_win = self.game.compare_cards()
            if round_win == 0:  # war
                self.game.war_cards.append(self.game.card_one)
                self.game.war_cards.append(self.game.card_two)
                for i in range(3):
                    self.game.war()
            elif round_win == 1:  # player1 wins
                self.game.add_cards_to_deck(self.game.hand_one)
                self.game.display_cards_left(self.player1, self.player2)
            elif round_win == 2:  # player2 wins
                self.game.add_cards_to_deck(self.game.hand_two)
                self.game.display_cards_left(self.player1, self.player2)
            winner = self.game.win_check()
            if winner == '1':
                print(f'\n{self.player1} WINS!')
            elif winner == '2':
                print(f'\n{self.player2} WINS!')

    def do_rules(self, _):
        """Show the rules of the game."""
        self.game.print_rules()
    
    def do_exit(self, _):
        """Leave the game."""
        print('\n\n B    Y    E \n')
        return True
    


    