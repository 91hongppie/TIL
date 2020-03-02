import sys
sys.stdin = open('SWEA_4008_숫자 만들기.txt', 'r')

def made(nums, result):
    global max_result, min_result
    if nums == len(numbers):
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for k in range(4):
        if operators[k] > 0:
            operators[k] -= 1
            if k == 0:
                made(nums+1, result+numbers[nums])
            elif k == 1:
                made(nums+1, result-numbers[nums])
            elif k == 2:
                made(nums+1, result*numbers[nums])
            elif k == 3:
                made(nums+1, int(result/numbers[nums]))
            operators[k] += 1
N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    max_result = -1e9
    min_result = 1e9
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    modify = []
    modify.append(numbers[0])
    made(1, numbers[0])
    fin_result = max_result - min_result
    print('#{} {}'.format(tc, fin_result))
