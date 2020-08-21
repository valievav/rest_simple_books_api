from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

