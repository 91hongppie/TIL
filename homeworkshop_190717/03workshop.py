text = input()

def palindrome(a):
    result = ''
    for i in range(0,len(a)):
        if a[i] == a[len(a)-1-i]:
            result += a[i]
    if result == a:
        return True
    else:
        return False

result = palindrome(text)
print(result)