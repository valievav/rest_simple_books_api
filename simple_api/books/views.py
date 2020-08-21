from rest_framework import viewsets
from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer = AuthorSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

