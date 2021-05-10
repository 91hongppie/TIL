```python
02homework
1.
mutable = List, Set, Dictionary(value만)
immutable = String, Tuple, Range
2.
numbers = list(range(1, 51))
print(numbers[0::2])
3.
classroom={'박홍은': 24, '이병주': 27, '조규홍': 29}
```

```python
02workshop
1.
n = 5
m = 9
i = '*'
for num in range(m):
    print(i*n)
    
# 강사님 풀이
m=9
n=5
for i in range(m):
    for j in range(n):
        print('*', end='')
    print()
    
2.
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
total_score = 0
score = student.values()
for i in score:
    total_score+=i
print(total_score)
print(total_score/len(student))
# 강사님 풀이
sum(student.values()) / len(student.values())
3.
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
people={}
for i in blood_types:
    if i in people:
        people[i]+=1
    else:
        people[i] = 1
print(people)
# 강사님 풀이
1.
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
blood_dict = {}
for blood in blood_types:
    if blood_dict.get(blood):
        blood_dict[blood] += 1
    else:
        blood_dict[blood] = 1
print(blood_dict)
2.
blood_dict = {}
for blood in blood_types:	
    blood_dict[blood] = blood_types.count(blood)
print(bloot.dict)
```

