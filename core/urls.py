from typing import List

from django.urls import path
from . import views

app_name: str = 'core'

urlpatterns: List = [
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]
