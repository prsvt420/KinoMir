from django.db.models import QuerySet

from core.models import Genre, Tag


class GenreService:
    """Сервис для работы с жанрами"""

    @staticmethod
    def get_genres() -> QuerySet[Genre]:
        """
        Метод возвращает список жанров

        Returns:
            QuerySet[Genre]: Список жанров
        """

        return Genre.objects.all()


class TagService:
    """Сервис для работы с тегами"""

    @staticmethod
    def get_tags() -> QuerySet[Tag]:
        """
        Метод возвращает список тегов

        Returns:
            QuerySet[Tag]: Список тегов
        """

        return Tag.objects.all()
