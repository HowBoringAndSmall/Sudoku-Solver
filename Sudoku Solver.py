def isValidSudoku(board):

    def check(board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if type(board[i][j]) is list:
                    return True
        return False

    def rotate_matrix(m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                board[i][j] = list(str(i) for i in range(1, 10))

    while check(board):
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if type(board[i][j]) is str and type(board[i][k]) is list and board[i][j] in board[i][k]:
                        board[i][k].remove(board[i][j])
        board = rotate_matrix(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                for k in range(len(board[i])):
                    if type(board[i][j]) is str and type(board[i][k]) is list and board[i][j] in board[i][k]:
                        board[i][k].remove(board[i][j])
        board = rotate_matrix(board)
        for n in range(0, 9, 3):
            for n1 in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            for k1 in range(3):
                                if type(board[i+n][j+n1]) is str and type(board[k+n][k1+n1]) is list and board[i+n][j+n1] in board[k+n][k1+n1]:
                                    board[k+n][k1+n1].remove(board[i+n][j+n1])
        for i in range(len(board)):
            for j in range(len(board[i])):
                if type(board[i][j]) is list and len(board[i][j]) == 1:
                    board[i][j] = board[i][j][0]
        print(board)
    return board
print(isValidSudoku([[".",".",".",".","7",".","4",".","."]
,["6","7","3",".",".",".",".",".","."]
,[".",".",".","3","9",".","5",".","."]
,["3",".","2",".",".",".",".",".","8"]
,[".",".","7",".","1",".",".",".","9"]
,[".",".",".","5",".","2",".",".","."]
,[".",".",".","2","5","8",".","3","."]
,[".",".",".",".",".","7",".","4","."]
,["8","6",".",".",".",".",".",".","."]]))