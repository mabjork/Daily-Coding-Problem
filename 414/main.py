
import math
import copy
N = 5

def generate_board(n):
    return [["."]*n for i in range(n)]

def print_board(board):
    for row in board:
        print(row)

def get_num_available(board):
    counter = 0
    for row in board:
        for val in row:
            if (val == "."):
                counter += 1
    return counter

def update_not_placable(board, x, y):
    if(board[y][x] == "."):
        board[y][x] = "-"

def place_queen(board, x, y):
    size = len(board)
    for i in range(size):
        update_not_placable(board, i, y)
        update_not_placable(board, x, i)
    
    for i in range(1, y+1):
        if (x - i >= 0):
            update_not_placable(board, x-i, y-i)
        if (x + i < size):
            update_not_placable(board, x+i, y-i)
    
    for i in range(1, size-y):
        if (x - i >= 0):
            update_not_placable(board, x-i, y+i)
        if (x + i < size):
            update_not_placable(board, x+i, y+i)
                    
    board[y][x] = "Q"

def get_available_positions(board):
    positions = []
    for r_index, row in enumerate(board):
        for c_index, val in enumerate(row):
            if (val == "."):
                positions.append((c_index, r_index))
    return positions

def get_available_positions_in_col(board, col):
    positions = []
    for row_index, row in enumerate(board):
        if(row[col] == "."):
            positions.append((col, row_index))
    return positions

def place_queens(board, starting_col = 0):
    if (starting_col == len(board)):
        return [board]
    finished_boards = []
    for col in range(starting_col, len(board)):
        available_possitions = get_available_positions_in_col(board, col)
        if(len(available_possitions) == 0):
            return []
        
        for pos in available_possitions:
            new_board = copy.deepcopy(board)
            place_queen(new_board, pos[0], pos[1])
            finished_boards.extend(place_queens(new_board, starting_col + 1))
    return finished_boards
        

board = generate_board(8)
finished_boards = place_queens(board)
print(len(finished_boards))