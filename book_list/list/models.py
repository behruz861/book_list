from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year_published = models.DateField()
    genres = models.ManyToManyField(Genre)
    rating = models.IntegerField(choices=zip(range(1, 11), range(1, 11)))
    views = models.IntegerField(default=0)