from django.contrib import admin
from .models import Author, Book, Genre


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name')
    list_display_links = ('first_name', 'second_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'year')
    list_display_links = ('name', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
