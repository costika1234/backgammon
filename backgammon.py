from constants import *
from utils import Utils

class Backgammon:
    def __init__(self, known_dice=[], known_moves=[], terminate_on_auto=False, suppress_output=False):
        # Assume turn is either 0 (white) or 1 (black).
        self.turn = 0

        # Player 1 (white) followed by player 2 (black).
        self.players = [list(INITIAL_POSITION), list(INITIAL_POSITION)]

        # List of non-generated dice.
        self.known_dice = known_dice

        # List of moves known in advance 
        self.known_moves = known_moves

        # Flag which specifies whether the game is terminated if given initial
        # moves and corresponding dice (useful for automated tests).
        self.terminate_on_auto = terminate_on_auto

        # Flag which specifies whether console output is suppressed or not.
        self.suppress_output = suppress_output

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
        dice = (0, 0)
        if len(self.known_dice) != 0:
            known_dice = self.known_dice[0]
            self.known_dice = self.known_dice[1:]
            dice = Utils.get_ordered_dice(known_dice)
        else:
            dice = Utils.roll_dice()

        Utils.print_to_console(
            "  You rolled [{0}-{1}]. Enter moves (space-separated)"
            ". Note: higher dice moved first (if possible)".format(dice[0], dice[1]),
            self.suppress_output)

        return dice

    def enter_moves(self):
        moves = ""
        if len(self.known_moves) != 0:
            moves = self.known_moves[0]
            self.known_moves = self.known_moves[1:] 
            moves = " ".join(map(str, list(moves)))
        else:
            moves = raw_input(SPACE_SEP * 4)

        Utils.print_to_console("    Your moves are: {0}\n".format(moves), self.suppress_output)

        return moves

    def get_play_mode(self):
        if len(self.known_moves) == len(self.known_dice) and len(self.known_moves) > 0:
            return AUTO
        elif len(self.known_moves) == 0 and self.terminate_on_auto:
            return EXIT
        else:
            return raw_input("Press 'r' to roll, 'x' to exit... ")

    def play(self):
        Utils.display_board(self.players, self.suppress_output)

        while True:
            mode = self.get_play_mode()

            if mode == ROLL or mode == AUTO:
                (dice1, dice2) = self.roll_dice()
                moves = self.enter_moves()
                self.perform_move(moves, dice1, dice2)
                self.change_turn()
                Utils.display_board(self.players, self.suppress_output)
            elif mode == EXIT:
                break
            else:
                print("Unknown command, try again.")
