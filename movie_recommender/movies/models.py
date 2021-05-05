from django.db import models
from django.contrib.auth.models import User 


class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    date_published = models.DateField()
    genre = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    director = models.CharField(max_length=255)


class View(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    num_rating = models.PositiveIntegerField()
    text_rating = models.TextField()