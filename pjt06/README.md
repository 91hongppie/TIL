# PJT_06 - 프레임워크 기반 웹 페이지 구현

## 1. 목표

- Python Web Framework 를 통한 데이터 조작
- Object Relational Mapping 에 대한 이해
- Template Variable 을 활용한 Template 제작
- Static 파일 관리

### models.py

```python
# movies/models.py
class Movie(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=50)
    watch_grade = models.CharField(max_length=50)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    score = models.FloatField()
```

- Movie - 영화 제목, 영화 제목(영어), 관객수, 개봉일, 장르, 관람 등급, 평점, 포스터 url, 줄거리
- Review - Movie의 외래키, 리뷰, 평점

## forms.py

```python
# movies.forms.py
from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'score')
```

- MovieForm - models.py 의 Movie 에서 받아온다.
- ReviewForm - models.py 의 Review 에서 받아온다

## views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()	
    context = {'movies': movies, }
    return render(request, 'movies/index.html', context)
# Movie 의 모든 것을 받아와서 index.html 에서 출력한다.

def create(request):
    if request.method == 'POST': # request 의 method 가 POST 인 경우에만 if 문 실행
        form = MovieForm(request.POST)
        if form.is_valid():	# form 의 유효성 검사
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/form.html', context
# 새 글을 작성할 때 POST 방식이 아니기 때문에 else 문이 실행되고 submit 을 누르면 POST 방식으로 들어오기 때문에 if 문이 실행된다.


def detail(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    reviews = movies.review_set.all()
    context = {'movie': movies, 'review_form': review_form, 'reviews': reviews,}
    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {'movie': movie, 'form':form}
    return render(request, 'movies/form.html', context)


def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
    return redirect('movies:index')

def reviews_create(request, movie_pk):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movie_pk
            review.save()
    return redirect('movies:detail', movie_pk)
# 리뷰를 작성할 때 어느 글에 리뷰를 작성하는 것인지 모르기 때문에 저장하기 전에 review.movie_id = movie_pk 를 통해 글의 번호를 review 에 추가하여 저장한다.
```

