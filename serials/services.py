from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import QuerySet

from core.models import Genre, Tag
from serials.models import Serial, SerialParticipant


class SerialService:
    """Сервис для работы с сериалами"""

    @staticmethod
    def get_serials() -> QuerySet[Serial]:
        """
        Метод возвращает список сериалов

        Returns:
            List[Serial]: Список сериалов
        """

        return Serial.objects.all().prefetch_related('genres').prefetch_related('tags')

    def get_serials_by_search_query(self, q: str) -> QuerySet[Serial]:
        """
        Метод возвращает список сериалов по поисковому запросу

        Returns:
            QuerySet[Serial]: Список сериалов по поисковому запросу
        """
        search_vector: SearchVector = SearchVector('title')
        search_query: SearchQuery = SearchQuery(q)

        return self.get_serials().annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query, cover_density=True),
        ).filter(search=search_query).order_by('-rank')

    @staticmethod
    def get_serial_participants(serial: Serial) -> QuerySet[SerialParticipant]:
        """
        Метод возвращает список участников сериала

        Returns:
            QuerySet[SerialParticipant]: Список участников сериала
        """

        return SerialParticipant.objects.filter(serial=serial).select_related('person')

    @staticmethod
    def get_genres(serial: Serial) -> QuerySet[Genre]:
        """
        Метод возвращает список жанров сериала

        Returns:
            QuerySet[Genre]: Список жанров сериала
        """

        return serial.genres.all()

    @staticmethod
    def get_tags(serial: Serial) -> QuerySet[Tag]:
        """
        Метод возвращает список тегов сериала

        Returns:
            QuerySet[Tag]: Список тегов сериала
        """

        return serial.tags.all()
