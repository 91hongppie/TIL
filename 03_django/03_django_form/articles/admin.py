from django.contrib import admin
from .models import Article, Comment, Hashtag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content',
                    'created_at', 'updated_at', 'user_id')


admin.site.register(Article, ArticleAdmin)

# 아래랑 동일한 코드 편한거 골라서 써
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id',)


# admin.site.register(Comment, CommentAdmin)

# 위와 동일한 코드 편한거 써라
@admin.register(Comment)
class Admin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at',
                    'updated_at', 'article_id', 'user_id',)


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Hashtag, HashtagAdmin)
