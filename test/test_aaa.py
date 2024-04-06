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

def test_solve_row3():
    assert solve_row([3], ["o", " ", " ", " "]) ==  ["o", "o", "o", "x"]

def test_solve_row4():
    assert solve_row([3], ["x", "o", " ", " ", " "]) == ["x", "o", "o", "o", "x"]

def test_solve_row5():
    assert solve_row([3], [" ", " ", " ", " ", "x"]) == [" ", "o", "o", " ", "x"]

def test_solve_row6():
    assert solve_row([3], ["x", " ", " ", " ", "x"]) == ["x", "o", "o", "o", "x"]

def test_solve_row7():
    assert solve_row([2], [" ", " ", "o", " ", " "]) == ["x", " ", "o", " ", "x"]
# def test_solve_row4():
#     assert solve_row([1, 1], [" ", " ", " "]) == ["o", "x", "o"]