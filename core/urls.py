from typing import List

from django.urls import path

from KinoMir import settings
from . import views

app_name: str = 'core'

urlpatterns: List = [
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]

if settings.DEBUG:
    urlpatterns.append(
        path('', views.redirect_to_movies_list, name='redirect_to_movies_list'),
    )
