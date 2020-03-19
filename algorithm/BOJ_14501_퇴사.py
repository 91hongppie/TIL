import sys
sys.stdin = open('BOJ_14501_퇴사.txt', 'r')

def cal(mon, pay):
    global result
    if mon == N:
        result = max(result, pay)
        return
    elif mon > N:
        return


    cal(mon+board[mon][0], pay+board[mon][1])
    cal(mon+1, pay)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
cal(0, 0)
print(result)