from collections import deque
def solution(maps):
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    Q = deque()
    lengthBoard = [[0 for i in range(len(maps[0]))] for _ in range(len(maps))]
    lengthBoard[0][0] = 1
    Q.append([0, 0, 1])
    while Q:
        x, y, dis = Q.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < len(maps) and 0 <= newY < len(maps[0]) and maps[newX][newY] == 1:
                if lengthBoard[newX][newY] == 0 or lengthBoard[newX][newY] > dis + 1:
                    lengthBoard[newX][newY] = dis + 1
                    Q.append([newX, newY, dis+1])
                
    answer = lengthBoard[-1][-1]
    if answer == 0:
        answer = -1
    return answer