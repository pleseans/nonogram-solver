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
  2  1
2 o  o
1 o
"""
def nonogram_solver(a,c):
    board = [
        [' ',' '],
        [' ',' ']
    ]
    
    for i in range(2):
        if a[i] == len(board[i]):
            board[i][1] = "o"
            board[i][0] = "o"
        elif a[i] != len(board[i]):
            pass

    for i in range(2):
        if c[i] == len(board[i][0]) and c[i] == len(board[i][1]):
            board[i][0] = "o"
            board[i][0] = "o"
        elif c[i] != len(board[i]):
            pass

    for i in range(len(board)):
        for j in range(len(board[i])):    
            if board[i][j] != 'o':
                board[i][j] = "x"

    print("",board[0],"\n",board[1])
    return board

