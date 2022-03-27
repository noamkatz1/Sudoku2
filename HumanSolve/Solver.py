import numpy as np
from random import sample
from generator import generator

def arrange_rows(board,areas):
    for row in range(9):
        area = {}
        area["element"] = "row"
        area["size"] = len(board[row]) - board[row].count(0)
        area["loc"] = row
        insert_in_order(area, areas)

def arrange_cols(board,areas):
    for col in range(9):
        emp_loc = 0
        for row in range(9):
            if board[row][col] != 0:
                emp_loc += 1
        area = {}
        area["element"] = "col"
        area["size"] = emp_loc
        area["loc"] = col
        insert_in_order(area, areas)
    
def arrange_squares(board,areas):
    for square in find_square():
        emp_loc = 0 
        for row in range(square["first_row"], square["last_row"]+1):
            for col in range(square["first_col"], square["last_col"]+1):
                if board[row][col] != 0:
                    emp_loc += 1
        area = {}
        area["element"] = "square"
        area["size"] = emp_loc
        area["loc"] = tuple(square.values())
        insert_in_order(area, areas)
        
# look at all the elements in the board, and describe the location and n of places to fill in them
def calculate_areas(board):
    areas = []
    arrange_rows(board,areas)
    arrange_cols(board,areas)
    arrange_squares(board,areas)
    return areas

# we need the elements in a certain order, here make sure every col row ans square is in order
def insert_in_order(area, areas):
    if len(areas) == 0:
        areas.append(area)
    else:
        is_in = False
        for i in range(len(areas)):
            if area["size"] > areas[i]["size"]:
                areas.insert(i, area)
                is_in = True
                break
            else:
                continue
        if not is_in:
            areas.append(area)

# location is set by the first row and last row with the first colmn and the last column
def find_square():
    first_row  = 0
    last_row   = 2
    first_col  = 0
    last_col   = 2
    square_loc = []
    
    while len(square_loc) < 9:
        square_loc.append({
          "first_row" : first_row,
          "last_row" : last_row,
          "first_col": first_col,
          "last_col" : last_col
        })
        if first_col < 6 and last_col < 8:
            first_col += 3
            last_col  += 3
        else:
            first_col  = 0
            last_col   = 2
            first_row  += 3
            last_row   += 3

    return square_loc

# now look for all an empty space, and see if a certain option is in the col,row and square. If not, keep. if its is, remove.
# when there is only one option - fill the space with the last option
def insert_options(board, row, col):
    if board[row][col] == 0:
        row_elements    = get_area_elements("row", row, col, board)
        col_elements    = get_area_elements("col", row, col, board)
        square_elements = get_area_elements("square", row, col, board)
        ns      = [n for n in range(1, 10)]
        options = [i for i in range(1, 10)]
        for opt in ns:
            if (opt in row_elements) or (opt in col_elements) or (opt in square_elements):
                options.remove(opt)
        if len(options) == 1:
            board[row][col] = options[0]
            
def check_row(board,elements,row):
    for col in range(9):
        if board[row][col] != 0:
            elements.append(board[row][col])
    return elements

def check_col(board,elements,col):
    for row in range(9):
        if board[row][col] != 0:
            elements.append(board[row][col])
    return elements

def check_square(board,elements,row,col):
    square_locs = find_square()
    for square in square_locs:
        if (square["first_row"] <= row <= square["last_row"]) and (square["first_col"] <= col <= square["last_col"]):
            for row in range(square["first_row"], square["last_row"]+1):
                for col in range(square["first_col"], square["last_col"]+1):
                    if board[row][col] != 0:
                        elements.append(board[row][col])
            break
    return elements
    
# find all the numbers in the elements that are not zero, and return them as a list

def get_area_elements(area_type, row, col, board):
    elements = []
    if area_type == "col":
        elements = check_col(board,elements,col)
                
    elif area_type == "row":
        elements = check_row(board,elements,row)
        
    elif area_type == "square":
        elements = check_square(board,elements,row,col)
    return elements


def insert_row(row,board):
    for col in range(9):
        insert_options(board, row, col)    

def insert_col(col,board):
    for row in range(9):
        insert_options(board, row, col)    

def insert_square(sqr,board):        
    first_row = sqr[0]
    last_row = sqr[1]
    first_col = sqr[2]
    last_col = sqr[3]
    for row in range(first_row, last_row+1):
        for col in range(first_col, last_col+1):
            insert_options(board, row, col)
    
def fill_board2(board):
    for _ in range(0, 3):
        areas = calculate_areas(board)
        for area in areas:
            if area["element"] == "row":
                insert_row(area["loc"],board)
            elif area["element"] == "col":
                insert_col(area["loc"],board)
            else:
                insert_square(area["loc"],board)
    return board

if __name__ == '__main__':
    board = generator()
  
    print("Puzzle:",np.matrix(board))
    board = fill_board2(board)


    print("Solution:",np.matrix(board))

