import sys
sys.stdin = open('BOJ_17136_색종이붙이기.txt', 'r')

from collections import deque
board = [list(map(int, input().split())) for _ in range(10)]
check = [[False for _ in range(10)] for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
dirCheck = [[0, 1], [1, 1], [1, 0]]
papers = []
answer = 0

def checkPaper(i, j, paperVolume):
    for k in range(1, 6):
        for l in range(k+1):
            if 0 <= i+l < 10 and 0<= j+k < 10 and 0<= i+k < 10:
                if board[i+l][j+k] != 1:
                    papers.append([k, i, j])
                    return 
                if board[i+k][j+l] != 1:
                    papers.append([k, i, j])
                    return 
            else:
                papers.append([k, i, j])
                return
        papers.append([k, i, j])

for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            papers.append([1, i, j])
            checkPaper(i, j, 1)
papers.sort(reverse=True)
result = 1e9
def cover(idx, newBoard, count, newPaper):
    global result
    if idx == len(paper):
        return
    sumNewBoard = 0
    for i in range(10):
        sumNewBoard += sum(newBoard[i])
    if sumNewBoard == 0:
        result = min(count, result)
        return
    cover(idx+1, newBoard, count, newPaper)
    size, x, y = papers[idx]
    contiCheck = 0
    if newPaper[size] != 0:
        for j in range(size):
            if sum(newBoard[x+j][y:y+size]) != size:
                contiCheck = 1
                break
        if contiCheck == 0:
            for j in range(size):
                for k in range(size):
                    newBoard[x+j][y+k] = 0
            newPaper[size] -= 1
            cover(idx+1, newBoard, count, newPaper)
            for j in range(size):
                for k in range(size):
                    newBoard[x+j][y+k] = 1
print(len(papers))
cover(0, board, 0, paper)
if result == 1e9:
    print(-1)
else:
    print(result)
                

