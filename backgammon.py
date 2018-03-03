from constants import *
from utils import Utils

class Backgammon:
    def __init__(self, manual_dice=[], debug_mode=False):
        # Assume turn is either 0 (white) or 1 (black).
        self.turn = 0

        # Player 1 (white) followed by player 2 (black).
        self.players = [list(INITIAL_POSITION), list(INITIAL_POSITION)]

        # List of non-generated dice.
        self.manual_dice = manual_dice

        # Flag to enable debug information.
        self.debug_mode = debug_mode

    def change_turn(self):
        self.turn = (self.turn + 1) % 2

    def perform_move(self, moves, dice1, dice2):
        # Dumb movements for now (TODO: implement properly).
        # Always assume that dice1 >= dice2.

        # Split the moves input and convert to the perspective of the current player.
        if self.turn == 0:
            moves = [int(i) - 1 for i in moves.split()]
        else:
            moves = [(NO_PIECES - int(i)) for i in moves.split()]
        
        no_moves = 4 if dice1 == dice2 else 2
        player_to_move = self.players[self.turn]

        for i in range(no_moves):
            player_to_move[moves[i]] -= 1
            
        player_to_move[moves[0] - dice1] += 1
        if no_moves == 2:
            player_to_move[moves[1] - dice2] += 1
        else:
            player_to_move[moves[1] - dice1] += 1
            player_to_move[moves[2] - dice1] += 1
            player_to_move[moves[3] - dice1] += 1
            
    def roll_dice(self):
        if len(self.manual_dice) != 0:
            dice = self.manual_dice[0]
            self.manual_dice = self.manual_dice[1:]
            return dice
        else:
            return Utils.roll_dice()


    def play(self):
        print("Backgammon Game\n")
        Utils.display_board(self.players)

        while True:
            key = raw_input("Press 'r' to roll, 'x' to exit... ")

            if key == "r":
                (dice1, dice2) = self.roll_dice()
                print("  You rolled [{0}-{1}]. Enter moves (space-separated). Note: higher dice moved first.".format(dice1, dice2))

                moves = raw_input(SPACE_SEP * 4)
                print("  Your moves are: {0}\n".format(moves))

                self.perform_move(moves, dice1, dice2)
                self.change_turn()

                Utils.display_board(self.players)
            elif key == "x":
                break
            else:
                print("Unknown command, try again.")
