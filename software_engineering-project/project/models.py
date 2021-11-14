from django.db import models


class Movie(models.Model):
    movietype = models.CharField(null=False, blank=False, max_length=30)
    title = models.CharField(null=False, blank=False, max_length=100)
    director = models.TextField(null=True, blank=True)
    cast = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=False, blank=False)
    rating = models.CharField(null=False, blank=False, max_length=15)

    def __str__(self):
        return self.title

