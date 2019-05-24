from django.db import models
# from django.utils import timezone




class Movie(models.Model):
    Title = models.TextField()
    Year = models.TextField(blank=True)
    Rated = models.TextField(blank=True)
    Released = models.TextField(blank=True)
    Runtime = models.TextField(blank=True)
    Genre = models.TextField(blank=True)
    Director = models.TextField(blank=True)
    Writer = models.TextField(blank=True)
    Actors = models.TextField(blank=True)
    Plot = models.TextField(blank=True)
    Language = models.TextField(blank=True)
    Country = models.TextField(blank=True)
    Awards = models.TextField(blank=True)
    Poster = models.URLField(max_length=255, blank=True)
    # Ratings = models.TextField(blank=True)
    Metascore = models.TextField(blank=True)
    imdbRating = models.TextField(blank=True)
    imdbVotes = models.TextField(blank=True)
    imdbID = models.TextField(blank=True)
    Type = models.TextField(blank=True)
    DVD = models.TextField(blank=True)
    BoxOffice = models.TextField(blank=True)
    Production = models.TextField(blank=True)
    Website = models.TextField(blank=True)
    Response = models.TextField(blank=True)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie', null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text