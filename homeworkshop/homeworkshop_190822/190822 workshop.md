# 190822 workshop

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    age = models.IntegerField()


    def __str__(self):
        return self.name
```

