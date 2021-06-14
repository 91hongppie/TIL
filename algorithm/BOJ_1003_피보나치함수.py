import sys
sys.stdin = open('BOJ_1003_피보나치함수.txt', 'r')

N = int(input())

for _ in range(N):
    num = int(input())
    if num == 0:
        print("1 0")
        continue
    elif num == 1:
        print("0 1")
        continue
    else:
        stack = [1, 1]

        while len(stack) != num:
            stack.append(stack[-1] + stack[-2])
        print("{} {}".format(stack[-2], stack[-1]))
