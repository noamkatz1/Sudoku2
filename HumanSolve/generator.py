import numpy as np
from random import sample

def generator():
    s1 = range(3)
    s2 = range(1,3*3+1)
    rows  = [ dis*3 + row for dis in sample(s1,len(s1)) for row in sample(s1,len(s1)) ] 
    cols  = [ dis*3 + col for dis in sample(s1,len(s1)) for col in sample(s1,len(s1)) ]
    instegers  = sample(s2,len(s2))

    index_finder = lambda row,col : (3*(row%3)+row//3+col)%9
    board = [ [instegers[index_finder(row,col)] for col in cols] for row in rows ]

    locations = 81
    emp_space = locations * 3//9
    for elm in sample(range(locations),emp_space):
        board[elm//9][elm%9] = 0
        
    return board