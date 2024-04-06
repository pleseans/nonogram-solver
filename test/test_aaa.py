from src.nonogram_solver import nonogram_solver, solve_row

def xtest_nonogaram_solver1():
    a = [2,1]
    c = [2,1]
    assert nonogram_solver(a,c) == [['o', 'o'],['o', 'x']]

def xtest_nonogaram_solver2():
    row = [3,2,1]
    col = [2,3,1]
    assert nonogram_solver(row,col) == [['o', 'o'],['o', 'x']]

"""
col   =    a b c

row   =  1
      =  2
      =  3

         
  2  3  1        
3 o  o  o
2 o  o
1    o     
         
         
         
"""

def test_solve_row1():
    assert solve_row([3], [" ", " ", " "]) == ["o", "o", "o"]

def test_solve_row2():
    assert solve_row([3], [" ", " ", " ", " "]) == [" ", "o", "o", " "]