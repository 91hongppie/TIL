import sys
sys.stdin = open('SWEA_1865_동철이의 일 분배.txt', 'r')

def DFS(num, per):
    global result
    if per <= result:
        return
    if num == rc:
        result = max(result, per)
        return
    for j in range(rc):
        if visit[j] == False:
            visit[j] = True
            DFS(num+1, per*board[num][j]/100)
            visit[j] = False


N = int(input())
for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [False] * rc
    result = 0
    DFS(0, 1)
    print('#{}'.format(tc), format(result*100, ".6f"))