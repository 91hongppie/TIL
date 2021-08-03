def fibonacci(num):
    if memoization[num]:
        return memoization[num]
    else:
        if num == 0:
            return memoization[0]
        elif num == 1:
            memoization[1] = 1
            return memoization[1]
        else:
            memoization[num] = fibonacci(num-1) + fibonacci(num-2)
            return memoization[num]


FIBO_SIZE = 10000
memoization= [0 for _ in range(FIBO_SIZE+1)]
print(fibonacci(100))
print(fibonacci(200))


left = 1
right = 1
for i in range(200):
    temp = right
    right += left
    left = temp
print(right)

