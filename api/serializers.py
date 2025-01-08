from typing import List

from rest_framework import serializers

from core.models import Genre, Tag
from movies.models import Movie
from movies.services import MovieService
from serials.models import Serial
from serials.services import SerialService


class MovieSerializer(serializers.ModelSerializer):
    """Сериализатор фильмов"""

    genres: serializers.SerializerMethodField = serializers.SerializerMethodField()
    tags: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model: type = Movie
        fields: str = "__all__"

    @staticmethod
    def get_genres(obj: Movie) -> List[Genre]:
        return [genre.title for genre in MovieService.get_genres(obj)]

    @staticmethod
    def get_tags(obj: Movie) -> List[Tag]:
        return [tag.title for tag in MovieService.get_tags(obj)]


class SerialSerializer(serializers.ModelSerializer):
    """Сериализатор сериалов"""

    genres: serializers.SerializerMethodField = serializers.SerializerMethodField()
    tags: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model: type = Serial
        fields: str = "__all__"

    @staticmethod
    def get_genres(obj: Serial) -> List[Genre]:
        return [genre.title for genre in SerialService.get_genres(obj)]

    @staticmethod
    def get_tags(obj: Serial) -> List[Tag]:
        return [tag.title for tag in SerialService.get_tags(obj)]
