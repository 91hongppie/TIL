from pprint import pprint
from copy import deepcopy

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

answer = 0
pocket = []
for i in moves:
    j = i - 1
    for k in range(len(board)):
        if board[k][j] != 0:     
            if len(pocket) > 0 and pocket[-1] == board[k][j]:
                answer += 2
                pocket.pop()
            else:
                pocket.append(board[k][j])
            board[k][j] = 0
            break    
