from src.nonogram_solver import nonogram_solver

def test_nonogaram_solver1():
    a = [2,1]
    c = [2,1]
    assert nonogram_solver(a,c) == [['o', 'o'],['o', 'x']]