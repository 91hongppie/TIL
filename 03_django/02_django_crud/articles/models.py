from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20) # blank=True 는 빈 값 허용 blank=False 가 기본값
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title