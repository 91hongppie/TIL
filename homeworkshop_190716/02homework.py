numbers = list(range(1, 51))
print(numbers[0::2])

classroom={'박홍은': 24, '이병주': 27, '조규홍': 29}
print(classroom)

m=9
n=5
for i in range(m):
    for j in range(n):
        print('*', end='')
    print()

student = {
    'python': 80, 
    'algorithm': 99, 
    'django': 89, 
    'flask': 83
}
total_score = 0
score = student.values()
for i in score:
    total_score+=i
print(total_score)
print(total_score/len(student))

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
people={}
for i in blood_types:
    if i in people:
        people[i]+=1
    else:
        people[i] = 1
print(people)