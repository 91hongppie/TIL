def findGCDAndLCM(num1, num2):
    global gcd, lcm
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break
    lcm = int((num1 * num2) / gcd)



gcd = 0
lcm = 0
findGCDAndLCM(8, 10)
print(gcd, lcm)