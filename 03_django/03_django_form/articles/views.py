from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Article, Comment
from .forms import ArticleForm

# Create your views here.


def index(request):
    # models 에서 뒤집어서 받기 때문에 order_by('pk') 필요없다.
    articles = Article.objects.all()
    # articles = get_list_or_404(Article)
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding)
        # 이 처리과정은 binding 이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        # form.is_valid() 로 form 이 유효한지 체크한다.
        if form.is_valid():
            article = form.save()
            # form.cleaned_data 로 정제된 데이터를 받는다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            # return redirect('articles:index') # get_absolute_url 안 썼을 때
            return redirect(article)
    else:
        form = ArticleForm()
    # 상황에 따라 context 에 넘어가는 2가지 form
    # 1. GET : 기본 form
    # 2. POST : 검증에 실패 후의 form(is_valid == False)
    context = {'form': form, }
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    # article = Article.objects.get(pk=article_pk)

    context = {'article': article, }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')

            article = form.save()
            return redirect(article)
    else:
        # articleForm 을 초기화 (이전에 DB에 저장된 )
        form = ArticleForm(instance=article)
    # 1. POST : 검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기화된 form
    context = {'form': form, 'article': article, }
    return render(request, 'articles/form.html', context)


def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = CommentForm()
        if form.is_valid():
            form = f.save(commit=False)
            form.some_field = 'some_value'
            form.save()
            return redirect(article)
    else:
        return redirect(article)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('articles:detail', article_pk)
