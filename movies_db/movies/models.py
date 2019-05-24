from django.db import models
from django.utils import timezone




class Movie(models.Model):
    Title = models.TextField(max_length=255)
    Year = models.TextField(max_length=255, blank=True)
    Rated = models.TextField(max_length=255, blank=True)
    Released = models.TextField(max_length=255, blank=True)
    Runtime = models.TextField(max_length=255, blank=True)
    Genre = models.TextField(max_length=255, blank=True)
    Director = models.TextField(max_length=255, blank=True)
    Writer = models.TextField(max_length=255, blank=True)
    Actors = models.TextField(max_length=255, blank=True)
    Plot = models.TextField(max_length=255, blank=True)
    Language = models.TextField(max_length=255, blank=True)
    Country = models.TextField(max_length=255, blank=True)
    Awards = models.TextField(max_length=255, blank=True)
    Poster = models.URLField(max_length=255, blank=True)
    # Ratings = models.TextField(blank=True)
    Metascore = models.TextField(max_length=255, blank=True)
    imdbRating = models.TextField(max_length=255, blank=True)
    imdbVotes = models.TextField(max_length=255, blank=True)
    imdbID = models.TextField(max_length=255, blank=True)
    Type = models.TextField(max_length=255, blank=True)
    DVD = models.TextField(max_length=255, blank=True)
    BoxOffice = models.TextField(max_length=255, blank=True)
    Production = models.TextField(max_length=255, blank=True)
    Website = models.TextField(max_length=255, blank=True)
    Response = models.TextField(max_length=255, blank=True)
    Total_comments = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie', null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    text = models.TextField(max_length=255, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text