from django.contrib import admin
from .models import Article     # .models 명시적 상대경로 표현(현재 폴더의 models)

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성한다.
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',) # 튜플에 하나의 인자를 넣으면 반드시 뒤에 , 넣는다.
    list_display_links = ('content',) # 링크 걸어준다.
    list_editable = ('title',) # 바로 수정할 수 있다.
    list_per_page = 2 # 기본값 = 100


admin.site.register(Article, ArticleAdmin)
