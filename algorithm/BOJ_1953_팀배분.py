import sys
sys.stdin = open('BOJ_1953_팀배분.txt', 'r')

N = int(input())
team1 = []
team2 = []
for i in range(1, N+1):
    if i not in team1 and i not in team2:
        hatePeople = list(map(int, input().split()))
        hatePeopleNum = hatePeople[0]
        for j in range(1, hatePeopleNum+1):
            if hatePeople[j] not in team2 and i not in team2:
                team2.append(hatePeople[j])
                if i not in team1:
                    team1.append(i)
            elif hatePeople[j] not in team1 and i not in team1:
                team1.append(hatePeople[j])
                if i not in team2:
                    team2.append(i)
    else:
        hatePeople = list(map(int, input().split()))
        hatePeopleNum = hatePeople[0]
        for j in range(1, hatePeopleNum+1):
            if i in team1 and hatePeople[j] not in team2:
                team2.append(hatePeople[j])
            elif i in team2 and hatePeople[j] not in team1:
                team1.append(hatePeople[j])

print(len(team1))
print(' '.join(map(str, team1)))
print(len(team2))
print(' '.join(map(str, team2)))
