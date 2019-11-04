import hashlib
from django.http import JsonResponse, HttpResponseBadRequest
from IPython import embed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST  # post 요청만 받아준다..
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.


def index(request):
    # GRATAVAR
    # filter 작성하면 여기서 작성할 필요없음!!
    # if request.user.is_authenticated:
    #     gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest
    # else:
    #     gravatar_url = None

    # SESSION
    # 사용자가 사이트에 몇번 방문하는지 count 하기
    # session에 visits_num 키로 접근해 값을 가져온다.
    # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면(방문한적이 없다면) 0 값을 가져오도록 한다.
    # 해당 키(visits_num 가 없다면 새로 만들면서 0으로가져온다.
    visits_num = request.session.get('visits_num', 0)
    # 그리고 가져온 값을 session에 visits_num에 매번 1 씩 증가한 값으로 할당한다. (유저의 다음 방문을 위해 count 누적시킴)
    request.session['visits_num'] = visits_num + 1
    # admin 에서 로그아웃 하고 다시 들어가면 이전 count가 누적 되지 않고 새롭게 count 된다.
    # 누적시키고 싶으면 "https://docs.djangoproject.com/en/2.2/topics/http/sessions/" 참고하기....
    # session data 안에 있는 새로운 정보를 수정했다면 django 는 수정한 사실을 알아채지 못하기 때문에 다음과 같이 설정한다.
    request.session.modified = True

    articles = Article.objects.all()  # model에서 meta로 ordering 미리 해줌...(이미 역순으로 가져온다)
    # articles = get_list_or_404(Article) # 글이 하나도 없으면 에러 뜸.....
    context = {'articles': articles, 'visits_num': visits_num, }
    return render(request, 'articles/index.html', context)


@login_required  # 로그인된 사람만 create로 접근가능함
def create(request):
    # embed()
    if request.method == 'POST':
        # forms 작성 전
        # title instance
        # title = request.POST.get('title') # post로 들어오는 title 저장
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()

        # forms 작성 후
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다.(binding 작업)
        # 이 처리과정은 binding이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        # 인스턴스 생성(통째로 받아온다... -> FORM이 데이터에 맞춰서 알아서 매칭해줌)
        form = ArticleForm(request.POST)
        # article_form = get_user_model()
        # form이 유효한지 체크한다.(유효성 검사)
        if form.is_valid():
            # article = form.save() # 유효성 검사후 저장만 하면 된다(어느 필드에 있는지 model form을 쓰면 알게됨!)
            article = form.save(commit=False)   # article 객체만 만들고 저장은 안함
            article.user = request.user   # 왜래키값을 받고 저장!
            article.save()
            # hashtag 시작점 (글이 작성 된 후 써야하므로!)
            # 원래 있던 hashtag인지 아닌지 판단할 필요 있음.(get_or_create => 기존에 있다면 get, 없다면 create)
            for word in article.content.split():  # article의 content를 공백 기준으로 리스트로 변경
                if word.startswith('#'):    # '#'으로 시작하는 요소만 선택
                    # 튜플로 나옴.../ word랑 같은 해시태그를 찾는데 있으면 기존 객체(.get), 없으면 새로운 객체를 생성(.create)
                    hashtag, created = Hashtag.objects.get_or_create(
                        content=word)
                    # hashtag만 쓰면 나중에 hashtag[0]으로 해야 저장된 hashtag값 가져올 수 있음.
                    article.hashtags.add(hashtag)

            # form.cleaned_data로 정제된 데이터를 받는다.
            # title = form.cleaned_data.get('title') # 데이터 받아 저장.
            # content = form.cleaned_data.get('content')
            # 유효성 검사 끝났으므로..save 할 필요없이 바로 저장..
            # article = Article.objects.create(title=title, content=content)
        # return redirect('articles:index') # 글 작성되면  detail로...
            # get_absolute_url 작성하면 인스턴스 객체에 바로 넣을 수 있음
            return redirect(article)
    else:
        form = ArticleForm()  # 인스턴스 생성
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET: 기본 form
    # 2. POST: 검증에 실패 후의 form(is_valid == False)
    context = {'form': form, }
    return render(request, 'articles/form.html', context)  # get 방식일때...


def detail(request, article_pk):
    # try:
    article = get_object_or_404(Article, pk=article_pk)  # 모델 객체, 인자(parameter)
    # except Article.DoesNotExist:    # DNE 에러 발생시 404에러 발생시키고 저 문구 띄워줌/
    #     raise Http404('No Article matches the given query.')
    comments = article.comment_set.all()  # 모델명_set 으로 article 의 모든 댓글 가져온다!!
    # get_user_model()로 가져온다!!, user의 번호가 필요(user_id => foreign key로 접근)
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    comment_form = CommentForm()    # 댓글 폼(detail 에서 출력되야 하므로...여기 적어준다...)
    context = {'article': article, 'comment_form': comment_form,
               'comments': comments, 'person': person, }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:  # 인증된 사용자만 delete 가능!!
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:    # 자기가 작성한 글이면 삭제
            article.delete()
        else:
            return redirect(article)    # 자기 글이 아니면 삭제 불가능
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:  # 작성자와 현재유저가 같아야 수정 가능!!!
        if request.method == "POST":
            # request, instance 둘다 적어줘야함
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                # model forms 설정하면 cleaned_data 필요없음!
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                article.save()
                # hashtag 수정 => 기존 값 다 지우고 새로 만든다
                article.hashtags.clear()  # 기존 값 삭제
                # 새로 만들기
                for word in article.content.split():  # article의 content를 공백 기준으로 리스트로 변경
                    if word.startswith('#'):    # '#'으로 시작하는 요소만 선택
                        # 튜플로 나옴.../ word랑 같은 해시태그를 찾는데 있으면 기존 객체(.get), 없으면 새로운 객체를 생성(.create)
                        hashtag, created = Hashtag.objects.get_or_create(
                            content=word)
                        # hashtag만 쓰면 나중에 hashtag[0]으로 해야 저장된 hashtag값 가져올 수 있음.
                        article.hashtags.add(hashtag)
                return redirect(article)
        else:
            # ArticleForm 을 초기화 (이전에 DB에 저장된 데이터를 넣어준 상태)
            # form = ArticleForm(initial={'title': article.title, 'content': article.content,})# 이전 값들을 가져옴
            # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
            # form = ArticleForm(initial=article.__dict__)
            # model form쓰면 instance 로 이전 값 가져온다!!!
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')   # 동일 인물이 아니면 홈으로 보냄.
    # 1. POST : 검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기화된 form
    context = {'form': form, 'article': article, }
    # create랑 html 공유함!(둘 다 form을 사용하므로...)
    return render(request, 'articles/form.html', context)

# @login_required # @login_required 와 @require_POST를 함께 쓰면 login 에서 next로 넘어갈때 GET방식으로 넘어가게 되어 405에러 발생함...
@require_POST  # post 요청만 허용하고 나머지는 막음... / if 문으로 post, get 분기할 필요 없음!!
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)  # 데이터 받아오기(인스턴스)
        # 유효성 검사
        if comment_form.is_valid():
            # commit=False
            # 객체를 create 하지만, db에 레코드는 작성하지 않는다.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user = request.user  # comment.user에 request.user 넣고 저장!
            comment.save()
    return redirect('articles:detail', article_pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)  # 인증된 사용자

    # 인증안된 사용자 일때 (접근권한 없다는 에러 보여주기)
    return HttpResponse('You are Unauthorized', status=401)


@login_required
def like(request, article_pk):
    if request.is_ajax():
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            liked = False
        else:
            article.like_users.add(request.user)
            liked = True
        # user = request.user -> request.user를 user로 쓸 수 있음
        # 해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속유저가 있다면 좋아요를 취소
        # 해당 게시글의 모든 좋아요를 가져와야한다.
        # if request.user in article.like_users.all(): # 해당 유저가 그 글의 게시글에 좋아요 했는지 확인
        #     article.like_users.remove(request.user) # 좋아요 취소(삭제)
        # else:
        #     article.like_users.add(request.user) # 좋아요
        context = {'liked': liked, 'count': article.like_users.count(), }
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest


@login_required
def follow(request, article_pk, user_pk):  # article_pk 인자만 받아옴...
    # 게시글 유저(작성자)
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 접속 유저(로그인)
    user = request.user
    if person != user:  # 작성자와 로그인한 사람이 달라야 한다!
        # 내가(request.user) 게시글 유저(person.user) 팔로워 목록에 이미 존재한다면,
        # if user in person.followers.all(): 동일한 기능을 함.
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('articles:detail', article_pk)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    # hashtag가 달린 모든 게시글 가져오기 (최신글 순서로..)
    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag': hashtag, 'articles': articles, }
    return render(request, 'articles/hashtag.html', context)
