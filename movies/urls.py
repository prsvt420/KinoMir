from typing import List

from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name: str = 'movies'

urlpatterns: List = [
    path('', cache_page(60 * 60)(views.MoviesListView.as_view()), name='movies-list'),
    path('<slug:slug>/', cache_page(60 * 60)(views.MovieDetailView.as_view()), name='movie-detail'),
]
