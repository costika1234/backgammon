#!/usr/local/bin/python

import random

NO_PIECES = 24
NUMBERS_SPACING = 2
BOARD_HEIGHT = 13
BOARD_WIDTH = 10 * NUMBERS_SPACING + 31
HORIZONTAL_SEP = "-"
VERTICAL_SEP = "|"
SPACE_SEP = " "
WHITE_COLOUR = "W"
BLACK_COLOUR = "B"
INITIAL_POSITION = [0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0,
                    5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]

class Backgammon:
    def __init__(self, debug_mode=False):
        # Assume turn is either 0 (white) or 1 (black).
        self.turn = 0

        # Player 1 (white) followed by player 2 (black).
        self.players = [list(INITIAL_POSITION), list(INITIAL_POSITION)]

        # Flag to enable debug information.
        self.debug_mode = debug_mode

    def build_numbers_str(self, begin, end, step=1):
        numbers = "  "
        for i in range(begin, end, step):
            if i <= 9:
                numbers += " "
            numbers += str(i)

            if i == (begin + end) / 2 - step:
                numbers += "  " + VERTICAL_SEP + " "
            else:
                numbers += " " * NUMBERS_SPACING

        return numbers

    def build_line(self, whites, blacks, natural_line_no):
        line = VERTICAL_SEP + SPACE_SEP * 2

        for i in range(NO_PIECES / 2):
            if whites[i] > 0:
                line += WHITE_COLOUR if whites[i] >= natural_line_no else SPACE_SEP
            elif blacks[i] > 0:
                line += BLACK_COLOUR if blacks[i] >= natural_line_no else SPACE_SEP
            else:
                line += SPACE_SEP

            if i == NO_PIECES / 4 - 1:
                line += SPACE_SEP * 2 + VERTICAL_SEP + SPACE_SEP * 2
            elif i != NO_PIECES / 2 - 1:
                line += SPACE_SEP * (NUMBERS_SPACING + 1)
            else:
                line += SPACE_SEP * 2 + VERTICAL_SEP

        return line

    def display_board(self):
        #   Initial position:
        #
        #   13   14   15   16   17   18  | 19   20   21   22   23   24
        #  -------------------------------------------------------------
        # |  W                   B       |  B                        W  |
        # |  W                   B       |  B                        W  |
        # |  W                   B       |  B                           |
        # |  W                           |  B                           |
        # |  W                           |  B                           |
        # |                              |                              |
        # |                              |                              |
        # |                              |                              |
        # |  B                           |  W                           |
        # |  B                           |  W                           |
        # |  B                   W       |  W                           |
        # |  B                   W       |  W                        B  |
        # |  B                   W       |  W                        B  |
        #  -------------------------------------------------------------
        #   12   11   10    9    8    7  |  6    5    4    3    2    1
        #

        top_border = bottom_border = SPACE_SEP + HORIZONTAL_SEP * BOARD_WIDTH
        top_numbers = self.build_numbers_str(NO_PIECES / 2 + 1, NO_PIECES + 1)
        middle_line = VERTICAL_SEP + SPACE_SEP * (BOARD_WIDTH / 2) + VERTICAL_SEP \
                                   + SPACE_SEP * (BOARD_WIDTH / 2) + VERTICAL_SEP
        bottom_numbers = self.build_numbers_str(NO_PIECES / 2, 0, -1)

        print(top_numbers)
        print(top_border)

        for i in range(BOARD_HEIGHT / 2):
            print(self.build_line(self.players[0][12:], self.players[1][:12][::-1], i + 1))

        print(middle_line)

        for i in range(BOARD_HEIGHT / 2):
            print(self.build_line(self.players[0][:12][::-1], self.players[1][12:], (BOARD_HEIGHT / 2) - i))
        
        print(bottom_border)
        print(bottom_numbers)

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
        # Always return (max_dice, min_dice)
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        return (max(r1, r2), min(r1, r2))

    def play(self):
        print("Backgammon Game\n")
        self.display_board()

        while True:
            key = raw_input("Press 'r' to roll, 'x' to exit... ")

            if key == "r":
                (dice1, dice2) = self.roll_dice()
                print("  You rolled [{0}-{1}]. Enter moves (space-separated). Note: higher dice moved first.".format(dice1, dice2))

                moves = raw_input(SPACE_SEP * 4)
                print("  Your moves are: {0}\n".format(moves))

                self.perform_move(moves, dice1, dice2)
                self.display_board()
                self.change_turn()
            elif key == "x":
                break
            else:
                print("Unknown command, try again.")


def main():
    game = Backgammon()
    game.play()

if __name__ == "__main__":
    main()








