from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector)
from django.db.models import QuerySet

from core.models import Genre, Tag
from movies.models import FilmParticipant, Movie


class MovieService:
    """Сервис для работы с фильмами"""

    @staticmethod
    def get_movies() -> QuerySet[Movie]:
        """
        Метод возвращает список фильмов

        Returns:
            List[Movie]: Список фильмов
        """

        return Movie.objects.all().prefetch_related("genres").prefetch_related("tags")

    def get_movies_by_search_query(self, q: str) -> QuerySet[Movie]:
        """
        Метод возвращает список фильмов по поисковому запросу

        Returns:
            QuerySet[Movie]: Список фильмов по поисковому запросу
        """
        search_vector: SearchVector = SearchVector("title")
        search_query: SearchQuery = SearchQuery(q)

        return (
            self.get_movies()
            .annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query, cover_density=True),
            )
            .filter(search=search_query)
            .order_by("-rank")
        )

    @staticmethod
    def get_film_participants(movie: Movie) -> QuerySet[FilmParticipant]:
        """
        Метод возвращает список участников фильма

        Returns:
            QuerySet[FilmParticipant]: Список участников фильма
        """

        return FilmParticipant.objects.filter(movie=movie).select_related("person")

    @staticmethod
    def get_genres(movie: Movie) -> QuerySet[Genre]:
        """
        Метод возвращает список жанров фильма

        Returns:
            QuerySet[Genre]: Список жанров фильма
        """

        return movie.genres.all()

    @staticmethod
    def get_tags(movie: Movie) -> QuerySet[Tag]:
        """
        Метод возвращает список тегов фильма

        Returns:
            QuerySet[Tag]: Список тегов фильма
        """

        return movie.tags.all()
