from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import QuerySet

from core.models import Person
from movies.models import Movie, FilmParticipant


class MovieService:

    @staticmethod
    def get_movies() -> QuerySet[Movie]:
        """
        Метод возвращает список фильмов

        Returns:
            List[Movie]: Список фильмов
        """

        return Movie.objects.all().prefetch_related('genres').prefetch_related('tags')

    def get_movies_by_search_query(self, search_query: str) -> QuerySet[Movie]:
        """
        Метод возвращает список фильмов по поисковому запросу

        Returns:
            QuerySet[Movie]: Список фильмов по поисковому запросу
        """
        search_vector: SearchVector = SearchVector('title')
        search_query: SearchQuery = SearchQuery(search_query)

        return self.get_movies().annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query, cover_density=True),
        ).filter(search=search_query).order_by('-rank')

    @staticmethod
    def get_film_participants(movie: Movie) -> QuerySet[Person]:
        """
        Метод возвращает список участников фильма

        Returns:
            QuerySet[Person]: Список участников фильма
        """

        return FilmParticipant.objects.filter(movie=movie).select_related('person')
