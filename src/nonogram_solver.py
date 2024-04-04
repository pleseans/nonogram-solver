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
    if cond[0] == len(row):
        for j in range(len(row)):
            row[j] = "o"
    else:
        sd = 0 + cond[0] - 1
        et = len(row) - cond[0]
        for i in range(et, sd + 1):
            row[i] = "o"
    return row