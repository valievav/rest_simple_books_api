from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('authors', views.AuthorView)
router.register('books', views.BookView)
router.register('genre', views.GenreView)

urlpatterns = [
    path('', include(router.urls)),
]
