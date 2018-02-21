print("Backgammon Game\n")

NO_PIECES = 24
NUMBERS_SPACING = 2
BOARD_HEIGHT = 13
BOARD_WIDTH = 10 * NUMBERS_SPACING + 31
VERTICAL_SEP = "|"

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

def build_line(indices, natural_line_no):
    #line = str(natural_line_no)
    #if natural_line_no < 10:
    #    line += "*"
    line = "  "

    for i in range(len(indices)):
        if indices[i] >= natural_line_no:
            line += "W"
        else:
            line += " "

        if i == len(indices) / 2 - 1:
            line += "  |  "
        elif i != len(indices) - 1:
            line += " " * (NUMBERS_SPACING + 1)
        else:
            line += "  "

    return line

def display_board(whites, blacks):
#   13  14  15  16  17  18  | 19  20  21  22  23  24   
#  ---------------------------------------------------
# |**W***W***W***W***W***W**|**B***B***B***B***B***B**|
# |  W               B      |  B                   W  |
# |  W               B      |  B                      |
# |  W                      |  B                      |
# |  W                      |  B                      |
# |                         |                         |
# |                         |                         |
# |                         |                         |
# |  B                      |  W                      |
# |  B                      |  W                      |
# |  B               W      |  W                      |
# |  B               W      |  W                   B  |
# |  B               W      |  W                   B  |
#  ---------------------------------------------------
#   12  11  10   9   8   7  |  6   5   4   3   2   1

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

    top_border = bottom_border = " " + "-" * BOARD_WIDTH
    top_numbers = build_numbers_str(NO_PIECES / 2 + 1, NO_PIECES + 1)
    middle_line = VERTICAL_SEP + " " * (BOARD_WIDTH / 2) + VERTICAL_SEP + " " * (BOARD_WIDTH / 2) + VERTICAL_SEP
    bottom_numbers = build_numbers_str(NO_PIECES / 2, 0, -1)

    print(top_numbers)
    print(top_border)

    for i in range(BOARD_HEIGHT / 2):
        print(VERTICAL_SEP + build_line(whites[12:], i + 1) + VERTICAL_SEP)

    print(middle_line)

    for i in range(BOARD_HEIGHT / 2):
        print(VERTICAL_SEP + build_line(whites[:12][::-1], (BOARD_HEIGHT / 2) - i) + VERTICAL_SEP)
    
    print(bottom_border)
    print(bottom_numbers)

display_board([0, 0, 0, 0, 0, 5, 
               0, 3, 0, 0, 0, 0,
               5, 0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0, 2], 
               [])





