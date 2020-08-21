from rest_framework import serializers
from .models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'second_name')


class BookSerializer(serializers.HyperlinkedModelSerializer):  # using HyperLinked serializer to have url for each book
    author = serializers.StringRelatedField()  # add str author instead of id
    genre = serializers.StringRelatedField(many=True)  # add str genres instead of ids

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'year', 'genre', 'url')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')
