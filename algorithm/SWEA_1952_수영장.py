import sys
sys.stdin = open('SWEA_1952_수영장.txt', 'r')

def cal(mon, pay):
    global result
    if mon > 11:
        result = min(result, pay)
        return
    if calendar[mon] != 0:
        cal(mon+1, pay+d*calendar[mon])
        cal(mon+1, pay+m)
        cal(mon+3, pay+t_m)
    else:
        cal(mon+1, pay)

N = int(input())
for tc in range(1, N+1):
    d, m, t_m, y = map(int, input().split())
    calendar = list(map(int, input().split()))
    result = 1e9
    cal(0, 0)
    if result > y:
        print('#{} {}'.format(tc, y))
    else:
        print('#{} {}'.format(tc, result))