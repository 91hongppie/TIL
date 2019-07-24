```python
190724 workshop
class Circle:
    pi = 3.14
    x=0
    y=0
    r=0
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    def center(self):
        return(self.x, self.y)
```

```python
c1 = Circle(3, 2, 4)
c1.center(), c1.circumference(), c1.area()
((2, 4), 18.84, 28.259999999999998)
```

