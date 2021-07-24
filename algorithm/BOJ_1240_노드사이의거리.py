import sys
sys.stdin = open('BOJ_1240_노드사이의거리.txt', 'r')

from collections import deque
N, M = list(map(int, input().split()))
stack = [[] for _ in range(N+1)]
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N-1):
    fromPoint, toPoint, dis = list(map(int, input().split()))
    stack[fromPoint].append([toPoint, dis])
    stack[toPoint].append([fromPoint, dis])
    board[fromPoint][toPoint] = dis
    board[toPoint][fromPoint] = dis

def findRoad(start, end, dis):
    global board, stack
    Q = deque()
    Q.append([start, dis])
    while Q:
        fromPoint, newDis = Q.popleft()
        for i in stack[fromPoint]:
            toPoint, addDis = i
            if board[start][toPoint] == 0:
                if start == toPoint:
                    continue
                board[start][toPoint] = newDis + addDis
                board[toPoint][start] = newDis + addDis
                Q.append([toPoint, newDis+addDis])
            else:
                if board[start][toPoint] >= newDis + addDis:
                    board[start][toPoint] = newDis + addDis
                    board[toPoint][start] = newDis + addDis
                    Q.append([toPoint, newDis+addDis])

    

for _ in range(M):
    fromPoint, toPoint = list(map(int, input().split()))
    findRoad(toPoint, fromPoint, 0)
    print(board[fromPoint][toPoint])
