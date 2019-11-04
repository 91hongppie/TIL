from django.db import models
from django.urls import reverse
from django.conf import settings # 모델에서 User 불러오기..

# Create your models here.
# Article 보다 위에 있어야 참조 가능!!!
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 유저 모델 가져오기..
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True) # 비어있더라도 ''로 채워줌..
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    class Meta:
        ordering = ('-pk',)   # 나중에 쓴 글이 위로오게한다..

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"article_pk": self.pk})
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.content

