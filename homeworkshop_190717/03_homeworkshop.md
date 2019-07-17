```python
03homework
1.
dir(__builtins__)
list(), print(), dict(), str(), int()
2.
3
3.
None
```

```python
03workshop
text = input()

def palindrome(a):
    result = ''
    for i in range(0,len(a)):
        if a[i] == a[-1-i]:
            result += a[i]
    if result == a:
        return True
    else:
        return False

result = palindrome(text)
print(result)

#강사님 풀이 1
def is_palindrome(word):
    list_word = list(word)
    # 리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
    for i in range(len(list_word) // 2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True
#강사님 풀이 2
word = 'hihihihih'
word == word[::-1] # word를 거꾸로 배열 # pythonic!!!!
```

