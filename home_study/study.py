# def positive_sum(numbers):
#     sum = 0
#     for i in numbers:
#         if int(i) > 0:
#             sum += int(i)
#     return sum

# print(positive_sum([1, -4, 7, 12])) 
# print(positive_sum([-1, -2, -3, -4]))

# def calc(equation):
#     equation = equation.replace('+', ' +')
#     equation = equation.replace('-', ' -')
#     return sum(map(int, equation.split()))

# print(calc('123+2-124')) 
# print(calc('-12+12-7979+9191')) 
# print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

class Point:
    r = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point:({self.x}, {self.y})'

p1 = Point(3, 5) 
print(p1)

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def get_area(self):
        return 3.14*self.r**2

    def get_perimeter(self):
        return 2*3.14*self.r

    def get_center(self):
        return (self.center.x, self.center.y)

    def __str__(self):
        return f'Circle:({self.center.x}, {self.center.y}), r:{self.r}'

p1 = Point(0, 0) 
c1 = Circle(p1, 3) 
print(c1.get_area()) 
print(c1.get_perimeter()) 
print(c1.get_center()) 
print(c1) 
p2 = Point(4, 5) 
c2 = Circle(p2, 1) 
print(c2.get_area()) 
print(c2.get_perimeter()) 
print(c2.get_center()) 
print(c2)
