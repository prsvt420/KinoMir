from django_filters import rest_framework as filters

from core.services import GenreService, TagService
from movies.models import Movie
from serials.models import Serial


class MovieFilter(filters.FilterSet):
    """Фильтр фильмов"""

    year: filters.RangeFilter = filters.NumberFilter(
        field_name='year',
    )

    genres: filters.ModelMultipleChoiceFilter = filters.ModelMultipleChoiceFilter(
        field_name='genres__slug',
        queryset=GenreService.get_genres(),
        to_field_name='slug',
    )

    tags: filters.ModelMultipleChoiceFilter = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=TagService.get_tags(),
        to_field_name='tags__slug',
    )

    class Meta:
        model: type[Movie] = Movie
        fields: tuple = ('year', 'genres', 'tags')


class SerialFilter(filters.FilterSet):
    """Фильтр сериалов"""

    year: filters.RangeFilter = filters.NumberFilter(
        field_name='year',
    )

    genres: filters.ModelMultipleChoiceFilter = filters.ModelMultipleChoiceFilter(
        field_name='genres__slug',
        queryset=GenreService.get_genres(),
        to_field_name='slug',
    )

    tags: filters.ModelMultipleChoiceFilter = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=TagService.get_tags(),
        to_field_name='tags__slug',
    )

    class Meta:
        model: type[Serial] = Serial
        fields: tuple = ('year', 'genres', 'tags')
