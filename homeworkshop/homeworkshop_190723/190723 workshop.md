```python
190723 workshop.md
```

```python
calc.py

def calc_sum(num1, num2): 
    return num1 + num2
    

def calc_odd(num1, num2):
    return num1 - num2


def calc_multiply(num1, num2):
    return num1 * num2


def calc_divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return f'0으로는 나눌 수 없습니다.'
```

```python
import calc

print(calc.calc_divide(2, 0)) # 0으로는 나눌 수 없습니다.
print(calc.calc_multiply(2, 5))
print(calc.calc_odd(2, 6))
print(calc.calc_sum(2, 250))
```

