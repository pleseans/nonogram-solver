# tf = False
# a = []
# c = []
# while tf != True:
#     b = input()
#     if b != '/':
#         a.append(b)
#     elif b == '/':
#         tf = True
# tf = False
# while tf != True:
#     b = input()
#     if b != '/':
#         c.append(b)
#     elif b == '/':
#         tf = True


"""
  2  3  1
3 o  o  o
2 o  o
1    o
"""
from copy import deepcopy
def nonogram_solver(a,c):
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    l = []
    while True:
        for i in range(len(board[0])):
            if a[i] == len(board[i]):
                for j in range(len(board[i])):
                    board[i][j] = "o"
            elif len(board[0]) >= 3:
                if c[i] > len(board[i]) // 2 + c[i] - len(board[i]) // 2:
                    board[i][1] == "o"

        for i in range(len(board)):
            if c[i] == len(board):
                for j in range(len(board[i])):
                    board[j][i] = "o"
            elif len(board[0]) >= 3:
                if c[i] == len(board[i]) // 2 + c[i] - len(board[i]) // 2:
                    board[i][1] == "o"

        # for i in range(len(board)):
     
                
                

        for i in range(len(board)):
            for j in range(len(board[i])):    
                if board[i][j] != 'o':
                    board[i][j] = "x"
        for i in board:
            l.append(i)
        if len(l) == len(board[0]) * len(board):
            break

    return board
b = nonogram_solver([3,2,1],[2,3,1])
for i in b:
    print(i)


def solve_row(cond, row):


    # 채울 수 있는 칸은 o로 채운다
    sd = get_start_of_start(row) + cond[0] - 1
    et = get_end_of_end(row) - cond[0]
    for i in range(et, sd + 1):
        row[i] = "o"
    
    indx = row.index("o")
    end = indx + (cond[0] - 1)
    end2 = indx - (cond[0] - 1)
    l = deepcopy(row)
    for i in range(end2, end + 1):
        l[i] = "o"
    for i in range(len(l)):
        if l[i] == " ":
            row[i] = "x"
        

    for i in range(len(row)):
        if row[i] == " " and cond[0] == count_o(row):
            row[i] = "x"
    
    return row

def count_o(row):
    count = 0
    for i in range(len(row)):
        if row[i] == "o":
            count += 1
    return count

def get_start_of_start(row):
    ss = 0
    for i in range(len(row)):
        if row[i] == "x":
            ss += 1
        else: 
            break
    return ss

def get_end_of_end(row):
    ee = len(row)
    for i in range(len(row) - 1, 0, -1):
        if row[i] == "x":
            ee -= 1
        else:
            break
    return ee
