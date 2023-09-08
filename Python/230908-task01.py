# Task 1 - 08/09/2023 - Yulia
# https://www.codewars.com/kata/564e1d90c41a8423230000bc

# ---------------------- DESCRIPTION ----------------------

# Knight vs King

# On the chess board rows, denoted by numbers, are called ranks, and columns, denoted by a letter, are called files).

# You put a Knight and a King in the board.

# Complete the method that tell us which one can capture the other one.

# You are provided with two object array; each contains an integer (the rank, first item) and a string/char (the file, second item) to show the position of the pieces in the chess board.

# Return:

# "Knight" if the knight is putting the king in check,
# "King" if the king is attacking the knight
# "None" if none of the above occur
# Example:

# knight = [7, "B"], king = [6, "C"]  ---> "King"

# ===============  Slava ===============

def knight_vs_king(knight_position, king_position):
    diff_y = abs(knight_position[0] - king_position[0])
    diff_x = abs(ord(knight_position[1]) - ord(king_position[1]))

    if diff_x + diff_y <= 2 and (diff_x == 1 or diff_y == 1):
        return "King"

    if (diff_x == 2 and diff_y == 1) or (diff_x == 1 and diff_y == 2):
        return "Knight"

    return "None"


# ===============  Yuliia ===============
def knight_vs_king(knight_position, king_position):
    knight = [int(knight_position[0]), ord(knight_position[1]) - ord('A') + 1]
    king = [int(king_position[0]), ord(king_position[1]) - ord('A') + 1]
    if (abs(king[0] - knight[0]) == 2 and abs(king[1] - knight[1]) == 1) or (
            abs(king[0] - knight[0]) == 1 and abs(king[1] - knight[1]) == 2):
        return "Knight"
    elif abs(king[0] - knight[0]) <= 1 and abs(king[1] - knight[1]) <= 1:
        return "King"
    return "None"
