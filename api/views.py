from typing import Any

from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from api.filters import MovieFilter, SerialFilter
from api.serializers import MovieSerializer, SerialSerializer
from movies.models import Movie
from movies.services import MovieService
from serials.models import Serial
from serials.services import SerialService


class MovieViewSet(viewsets.ModelViewSet):
    """Api фильмов"""

    queryset: QuerySet[Movie] = MovieService().get_movies()
    serializer_class: type[BaseSerializer[Any]] | None = MovieSerializer
    filterset_class: type[MovieFilter] = MovieFilter

    @method_decorator(cache_page(60 * 60))
    def list(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)


class SerialViewSet(viewsets.ModelViewSet):
    """Api сериалов"""

    queryset: QuerySet[Serial] = SerialService().get_serials()
    serializer_class: type[BaseSerializer[Any]] | None = SerialSerializer
    filterset_class: type[SerialFilter] = SerialFilter

    @method_decorator(cache_page(60 * 60))
    def list(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)
