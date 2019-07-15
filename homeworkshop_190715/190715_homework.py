import keyword
print(keyword.kwlist)

a = 0.1 * 3
b = 0.3
print(a == b)


name = '철수'
print(f'안녕 {name}야')

n = 5
m = 9
print((('*'*n) + '\n')*m)


print(f'"파일은 C:\\Windows\\Users\\내문서\\python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')

a = 1
b = 4
c = -21
x_1 = (-b+(b**2 - 4*a*c)**(1/2))/2*a
x_2 = (-b-(b**2 - 4*a*c)**(1/2))/2*a
print(x_1, x_2)