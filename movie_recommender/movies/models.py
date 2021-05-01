from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    date_published = models.DateField()
    genre = models.CharField(max_length=255)
    duration = models.PositiveBigIntegerField()
    country = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
