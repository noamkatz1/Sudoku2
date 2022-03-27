import numpy as np
from generator import generator

def check_col(col,n,board):
    for i in range(9):
        if board[col][i] == n:
            return False
    return True

def check_row(row,n,board):
    for i in range(9):
        if board[i][row] == n:
            return False
    return True

def check_square(col,row,n,board):
    row_init = (row//3)*3
    col_init = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[col_init+i][row_init+j] == n:
                return False
    return True
    
def place_num(col,row,n,board):
    if not check_col(col,n,board):
        return False

    if not check_row(row,n,board):
        return False

    if not check_square(col,row,n,board):
        return False
    
    return True

def fill_board(board):
    for col in range(9):
        for row in range(9):
            if board[col][row] == 0:
                for n in range(1,10):
                    if place_num(col,row,n,board):
                        board[col][row] = n
                        fill_board(board)
                        board[col][row] = 0
                return
    print("Solution:",np.matrix(board))

if __name__ == '__main__':
    board = generator()
    print("Pazzle:",np.matrix(board))
    board = fill_board(board)