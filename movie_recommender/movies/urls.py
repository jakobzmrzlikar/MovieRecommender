from os import name
from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search, name="search_results"),
    path('info/<str:title>/', views.info, name="info")
]
