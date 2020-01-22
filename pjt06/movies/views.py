from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies, }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/form.html', context)


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

