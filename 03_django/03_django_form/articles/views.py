import hashlib
from IPython import embed
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
# Create your views here.


def index(request):
    visits_num = request.session.get('visits_num', 0)
    request.session['visits_num'] = visits_num + 1
    request.session.modified = True
    articles = Article.objects.all()
    context = {'articles': articles, 'visits_num': visits_num, }
    return render(request, 'articles/index.html', context)


# def index(request):
#     # embed()
#     # session 에 visits_num 키로 접근해 값을 가져온다.
#     # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면 (방문한 적이 없다면) 0 값을 가져오도록 한다.
#     visits_num = request.session.get('visits_num', 0)
#     # 그리고 가져온 값을 session 에 visits_num 에 매번 1씩 증가한 값으로 할당한다. (유저의 다음 방문을 위해)
#     request.session['visits_num'] = visits_num + 1
#     # session data 안에 있는 새로운 정보를 수정했다면 django 는 수정한 사실을 알아채지 못하기 때문에 다음과 같이 설정.
#     request.session.modified = True
#     # models 에서 뒤집어서 받기 때문에 order_by('pk') 필요없다.
#     articles = Article.objects.all()
#     # articles = get_list_or_404(Article)
#     context = {'articles': articles, 'visits_num': visits_num, }
#     return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding)
        # 이 처리과정은 binding 이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        # embed()
        # form.is_valid() 로 form 이 유효한지 체크한다.
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # 글이 db 에 등록된 이후에 해시태그 작성
            for word in article.content.split():  # content 를 공백 기준으로 리스트로 변경
                if word.startswith('#'):    # '#'으로 시작하는 요소만 선택
                    # word랑 같은 해시태그를 찾는데 있으면 기존 객체(.get), 없으면 새로운 객체를 생성(.create)
                    hashtag, created = Hashtag.objects.get_or_create(
                        content=word)
                    # created 를 사용하지 않았다면, article.hashtags.add(hashtag[0]) 를 쓴다.
                    article.hashtags.add(hashtag)

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
    comments = article.comment_set.all()  # article 의 모든 댓글
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    comment_form = CommentForm()  # 댓글 폼
    # article = Article.objects.get(pk=article_pk)

    context = {'article': article,
               'comment_form': comment_form, 'comments': comments, 'person': person, }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')

                article.save()
                # hashtag
                article.hashtags.clear()  # 해당 article 의 hashtag 전체 삭제
                for word in article.content.split():  # content 를 공백 기준으로 리스트로 변경
                    if word.startswith('#'):    # '#'으로 시작하는 요소만 선택
                        # word랑 같은 해시태그를 찾는데 있으면 기존 객체(.get), 없으면 새로운 객체를 생성(.create)
                        hashtag, created = Hashtag.objects.get_or_create(
                            content=word)
                        # created 를 사용하지 않았다면, article.hashtags.add(hashtag[0]) 를 쓴다.
                        article.hashtags.add(hashtag)
                return redirect(article)
        else:
            # articleForm 을 초기화 (이전에 DB에 저장된 )
            form = ArticleForm(instance=article)
        # 1. POST : 검증에 실패한 form(오류 메세지도 포함된 상태)
        # 2. GET : 초기화된 form
    else:
        return redirect('articles:index')
    context = {'form': form, 'article': article, }
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    # 405 error 때문에 @login_required 를 쓰지 않고 if request.user.is_authenticated: 를 쓴다.
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 객체를 Create 하지만, db 에 레코드는 작성하지 않는다.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
    return redirect('articles:detail', article_pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('FIRE!!!!!', status=401)


@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # get 을 쓰면 없을 때 오류가 난다. 그래서 filter 를 쓴다.
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

        #  해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속유저가 있다면 좋아요를 취소
    # if request.user in article.like_users.all():
    #     article.like_users.remove(request.user)  # 좋아요 취소
    # else:
    #     article.like_users.add(request.user)    # 좋아요
    return redirect('articles:index')


@login_required
def follow(request, article_pk, user_pk):
    # 게시글 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 접속 유저
    user = request.user
    # 내(request.user)가 게시글 유저 팔로워 목록에 이미 존재한다면,
    # if user in person.followers.all()
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('articles:detail', article_pk)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag': hashtag, 'articles': articles, }
    return render(request, 'articles/hashtag.html', context)
