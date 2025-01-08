from typing import List

from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name: str = "serials"

urlpatterns: List = [
    path("", cache_page(60 * 60)(views.SerialsListView.as_view()), name="serials-list"),
    path(
        "<slug:slug>/",
        cache_page(60 * 60)(views.SerialDetailView.as_view()),
        name="serial-detail",
    ),
]
