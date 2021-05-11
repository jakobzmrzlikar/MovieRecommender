from django.shortcuts import render

from .models import CollaborativeFilteringRecommender, TopRatedRecommender, MostViewedRecommender

def recommend(request):
    user_id = request.user.id
    recommender = MostViewedRecommender()
    context = {}
    context['movies'] = recommender.recommend(user_id)
    return render(request, 'recommender/movies.html', context)
