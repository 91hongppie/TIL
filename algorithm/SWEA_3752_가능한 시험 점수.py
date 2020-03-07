import sys
sys.stdin = open('SWEA_3752_가능한 시험 점수.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    problems = int(input())
    scores = list(map(int, input().split()))
    score_board = [0] * (sum(scores) + 1)
    score_board[0] = 1
    score_list = [0]
    for u in scores:
        p = len(score_list)
        for k in score_list[:p]:
            if score_board[u+k] == 0:
                score_board[u+k] = 1
                score_list.append(u+k)
    print('#{} {}'.format(tc, len(score_list)))
