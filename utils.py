import random

from constants import *

class Utils:
    @staticmethod
    def roll_dice():
        # Always return (max_dice, min_dice)
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        return (max(r1, r2), min(r1, r2))

    @staticmethod
    def build_numbers_str(begin, end, step=1):
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

    @staticmethod
    def build_line(whites, blacks, natural_line_no):
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

    @staticmethod
    def display_board(players):
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
        top_numbers = Utils.build_numbers_str(NO_PIECES / 2 + 1, NO_PIECES + 1)
        middle_line = VERTICAL_SEP + SPACE_SEP * (BOARD_WIDTH / 2) + VERTICAL_SEP \
                                   + SPACE_SEP * (BOARD_WIDTH / 2) + VERTICAL_SEP
        bottom_numbers = Utils.build_numbers_str(NO_PIECES / 2, 0, -1)

        print(top_numbers)
        print(top_border)

        for i in range(BOARD_HEIGHT / 2):
            print(Utils.build_line(players[0][12:], players[1][:12][::-1], i + 1))

        print(middle_line)

        for i in range(BOARD_HEIGHT / 2):
            print(Utils.build_line(players[0][:12][::-1], players[1][12:], (BOARD_HEIGHT / 2) - i))
        
        print(bottom_border)
        print(bottom_numbers)

