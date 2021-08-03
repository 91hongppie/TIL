def factorial(num):
    if memoization[num]:
        return memoization[num]
    else:
        if num == 0:
            memoization[num] = 1
            return memoization[num]
        elif num == 1:
            memoization[num] = 1
            return memoization[num]
        else:
            memoization[num] = num * factorial(num-1)
            return memoization[num]

memoization = [0 for _ in range(10000)]
print(factorial(100))
print(factorial(30))