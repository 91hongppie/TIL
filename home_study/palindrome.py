import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(100)]
    ans = 1

    # 한 행에 대해서
    for idx in range(100):
        for s in range(100):
            for e in range(99, s, -1):
                L = e - s + 1
                if ans >= L: break        
                for i in range(L//2):
                    if arr[idx][s + i] != arr[idx][e - i]: break
                else:
                    ans = L
                if ans >= L: break
                for i in range(L//2):
                    if arr[s + i][idx] != arr[e - i][idx]: break
                else:
                    ans = L
    print(ans)
