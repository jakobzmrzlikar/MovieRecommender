from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from django.shortcuts import render

from .models import Movie, View, Rating


def get_avg_rating(movie, context):
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('num_rating'))['num_rating__avg']
    if not avg_rating:
        context['has_ratings'] = False
    else:
        context['has_ratings'] = True
        context['avg_rating'] = round(avg_rating, 2)
    return context

def get_comments(movie, context):
    recent_comments = Rating.objects.filter(movie=movie).exclude(
        text_rating='').order_by('time').values_list('text_rating', flat=True)[:5]
    if not recent_comments:
        context['has_comments'] = False
    else:
        context['has_comments'] = True
        context['comments'] = recent_comments
    return context


@login_required
def index(request):
    return render(request, 'movies/index.html')


@login_required
def search(request):
    context = {}
    query = request.GET.get('search')
    if not query:
        return render(request, 'movies/index.html')
    context['movies'] = Movie.objects.filter(title__search=query)
    return render(request, 'movies/search_results.html', context)


@login_required
def info(request, title):
    user = request.user
    movie = Movie.objects.filter(title__search=title)[0]
    View.objects.create(movie=movie, user=user)
    context = {}
    context['movie'] = movie
    context['rated'] = False
    context = get_avg_rating(movie, context)
    context = get_comments(movie, context)
    return render(request, 'movies/info.html', context)


@login_required
def rate(request, title):    
    movie = Movie.objects.filter(title__search=title)[0]
    user = request.user
    num_rating = request.GET.get('num_rating')
    text_rating = request.GET.get('text_rating')
    Rating.objects.create(
        movie=movie,
        user=user,
        num_rating=num_rating,
        text_rating=text_rating
        )
    context = {}
    context['movie'] = movie
    context['rated'] = True
    context = get_avg_rating(movie, context)
    context = get_comments(movie, context)
    return render(request, 'movies/info.html', context)
