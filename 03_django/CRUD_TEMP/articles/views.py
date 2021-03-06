from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk') # DB 가 변경
    # articles = Article.objects.all()[::-1] # python 이 변경

    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def create(request):
    # CREATE
    if request.method == 'POST':
    # try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 1
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()
        
        # 2
        article = Article(title=title, content=content)
    #     article.full_clean() # 유효성 검증.
    # except ValidationError:
    #     raise ValidationError('Error')
    # else:
        article.save()
        return redirect(article) # 메인 페이지
    # 3
    # Article.objects.create(title=title, content=content)

    # NEW
    else:
        return render(request, 'articles/create.html')

        

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all() # article 에서 comment 모두 가져오기
    context = {'article': article, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index') # DB를 건드렸기 때문에 render은 옳지 않다.
    else:
        return redirect(article)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article,}
#     return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':     
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)

def comments_create(request, article_pk):
    # 댓글을 달 게시글
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # form 에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article)
        # get_absolute_url 구현 못했을 때
        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)
    else:
        return redirect(article)

def comments_delete(request, article_pk, comment_pk):
    # article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    # return redirect(article)
    return redirect('articles:detail', article_pk)