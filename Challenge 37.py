#Question 38

#This problem was asked by Microsoft.

# You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board 
# where N queens can be placed on the board without threatening each other,
# i.e. no two queens share the same row, column, or diagonal.

#Answer 38




def is_valid(board, row):
    if row in board:
        return False

    column = len(board)
    for occupied_column, occupied_row in enumerate(board):
        if abs(occupied_row - row) == abs(occupied_column - column):
            return False

    return True


def get_queen_configurations(board, n):
    if n == len(board):
        return 1

    count = 0
    for row in range(n):
        if is_valid(board, row):
            count += get_queen_configurations(board + [row], n)

    return count

############################################################################################################################
############################################################################################################################

assert not is_valid([0, 2], 0)
assert not is_valid([0, 2], 2)
assert is_valid([0, 8], 3)
assert not is_valid([1, 3], 2)
assert is_valid([], 1)

assert get_queen_configurations([], 2) == 0
assert get_queen_configurations([], 4) == 2
assert get_queen_configurations([], 5) == 10
assert get_queen_configurations([], 8) == 92
