from typing import List

from django.urls import path
from . import views

app_name: str = 'movies'

urlpatterns: List = [
    path('', views.MoviesListView.as_view(), name='movies-list'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie-detail'),
]
