```python
04homework
1.
Local scope
Enclosed scope
Global scope
Built-in scope
2.
1 
# 2개를 리턴하는 것처럼 보이지만 실제로는 튜플 1개가 리턴되는 것이고 이는 하나의 튜플 객체입니다.
3.
단점
작성하기 어려움. 메모리 스택이 넘치거나 프로그램이 느려지는 문제
장점
직관적이고 이해하기 쉬운 경우가 많음
(알고리즘에 경우)
```

```python
04workshop
import math
def root(n):
    small = float(n-1)
    big = float(n)    
    if n == 1:
        return n
    elif n <= 0:
        return f'양수를 입력해주세요.'
    else:
        while big - small > 1e-10:
            if n<((big+small)/2)**2:
                big = (big+small)/2
            elif n>((big+small)/2)**2:
                small = (big+small)/2
        return big

print(root(2))
print(math.sqrt(2))

# 강사님 풀이
# 양의 정수 n 을 입력 받아 제곱근의 근사값( 제곱했을 때 n이 되는 수) 를 반환하는 함수를 작성
def my_sqrt(n): # n = 2
    x, y = 1, n
    result = 1

    # 제곱근의 제곱(result**2)과 입력 값(n=2) 의 차이가 적어도 이 정도차이보다 작아지면!
    while abs(result**2 - n) > 1e-10: # 1e-10 == 1**-10
        result = (x+y)/2  # 양쪽 끝 값을 더해서 2로 나눈다.(절반을 구한다)
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다.
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))

def my_sqrt(n): # n = 2
    x, y = 1, n
    result = 1

    # 실수를 계산할 때 차이가 이정도면 거의 차이가 없는거라 그냥 같다고 보자!
    while not math.isclose(result**2, n): # not을 넣어줘야 무한루프에 안빠진다.
        result = (x+y)/2  # 양쪽 끝 값을 더해서 2로 나눈다.(절반을 구한다)
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다.
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))
```

