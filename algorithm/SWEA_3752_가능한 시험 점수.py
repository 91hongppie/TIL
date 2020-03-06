import sys
sys.stdin = open('SWEA_3752_가능한 시험 점수.txt', 'r')
from collections import deque

def grade(num, score):
    if num == problems:
        score_board[score] = 1
        return
    grade(num+1, score+scores[num])
    grade(num+1, score)


N = int(input())

for tc in range(1, N+1):
    problems = int(input())
    scores = list(map(int, input().split()))
    score_board = [0] * (sum(scores) + 1)
    print(score_board)
    score_list = set()
    grade(0, 0)
    print(score_board)