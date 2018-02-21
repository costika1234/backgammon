#!/usr/local/bin/python

import random

NO_PIECES = 24
NUMBERS_SPACING = 2
BOARD_HEIGHT = 13
BOARD_WIDTH = 10 * NUMBERS_SPACING + 31
HORIZNOTAL_SEP = "-"
VERTICAL_SEP = "|"
SPACE_SEP = " "
WHITE_COLOUR = "W"
BLACK_COLOUR = "B"
INITIAL_POSITION = [0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0,
                    5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]

class Backgammon:
    def __init__(self):
        pass

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
                if whites[i] >= natural_line_no:
                    line += WHITE_COLOUR
                else:
                    line += SPACE_SEP
            elif blacks[i] > 0:
                if blacks[i] >= natural_line_no:
                    line += BLACK_COLOUR
                else:
                    line += SPACE_SEP
            else:
                line += SPACE_SEP

            if i == NO_PIECES / 4 - 1:
                line += SPACE_SEP * 2 + VERTICAL_SEP + SPACE_SEP * 2
            elif i != NO_PIECES / 2 - 1:
                line += SPACE_SEP * (NUMBERS_SPACING + 1)
            else:
                line += SPACE_SEP * 2 + VERTICAL_SEP

        return line

    def display_board(self, whites, blacks):
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

        top_border = bottom_border = SPACE_SEP + HORIZNOTAL_SEP * BOARD_WIDTH
        top_numbers = self.build_numbers_str(NO_PIECES / 2 + 1, NO_PIECES + 1)
        middle_line = VERTICAL_SEP + SPACE_SEP * (BOARD_WIDTH / 2) + VERTICAL_SEP \
                                   + SPACE_SEP * (BOARD_WIDTH / 2) + VERTICAL_SEP
        bottom_numbers = self.build_numbers_str(NO_PIECES / 2, 0, -1)

        print(top_numbers)
        print(top_border)

        for i in range(BOARD_HEIGHT / 2):
            print(self.build_line(whites[12:], blacks[:12][::-1], i + 1))

        print(middle_line)

        for i in range(BOARD_HEIGHT / 2):
            print(self.build_line(whites[:12][::-1], blacks[12:], (BOARD_HEIGHT / 2) - i))
        
        print(bottom_border)
        print(bottom_numbers)

    def play(self):
        print("Backgammon Game\n")
        self.display_board(INITIAL_POSITION, INITIAL_POSITION)

        print("Press 'r' to roll, 'x' to exit...")

        while True:
            key = raw_input()

            if key == "r":
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print("  You rolled [{0}-{1}]".format(max(dice1, dice2), min(dice1, dice2)))
            elif key == "x":
                break
            else:
                print("Unknown command, try again.")


def main():
    game = Backgammon()
    game.play()

if __name__ == "__main__":
    main()








