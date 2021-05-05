from django.contrib.auth.decorators import login_required
from django.db.models import query

from django.shortcuts import render

from .models import Movie, View, Rating


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
    context = {}
    context['movie'] = Movie.objects.filter(title__search=title)[0]
    return render(request, 'movies/info.html', context)


@login_required
def rate(request):
    rating = request.GET.get('rating')
    Rating.objects.create()
