from typing import List

from django.urls import path
from . import views

app_name: str = 'serials'

urlpatterns: List = [
    path('', views.SerialsListView.as_view(), name='serials-list'),
    path('<slug:slug>/', views.SerialDetailView.as_view(), name='serial-detail'),
]
