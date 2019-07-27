a = '123-13+34-46-45+57+45'
b = a.replace('+', ',+')
b = b.replace('-', ',-')
b = b.split(',')
print(b)
c = 0
for i in range(len(b)):
    c += int(b[i])
print(c)