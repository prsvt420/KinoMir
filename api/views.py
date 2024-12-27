from typing import Any

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer

from api.filters import MovieFilter, SerialFilter
from api.serializers import MovieSerializer, SerialSerializer
from movies.models import Movie
from movies.services import MovieService
from serials.models import Serial
from serials.services import SerialService


class MovieViewSet(viewsets.ModelViewSet):
    """Представление API фильмов"""
    queryset: QuerySet[Movie] = MovieService().get_movies()
    serializer_class: type[BaseSerializer[Any]] | None = MovieSerializer
    filterset_class: type[MovieFilter] = MovieFilter


class SerialViewSet(viewsets.ModelViewSet):
    """Представление API сериалов"""

    queryset: QuerySet[Serial] = SerialService().get_serials()
    serializer_class: type[BaseSerializer[Any]] | None = SerialSerializer
    filterset_class: type[SerialFilter] = SerialFilter
