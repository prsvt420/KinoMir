from typing import Tuple

from django.db import models


class Person(models.Model):
    """Модель человека"""

    first_name: models.CharField = models.CharField(max_length=255, verbose_name='Имя')
    last_name: models.CharField = models.CharField(max_length=255, verbose_name='Фамилия')
    photo: models.ImageField = models.ImageField(
        upload_to='film_participants/',
        verbose_name='Фото',
        null=True,
        blank=True,
    )

    class Meta:
        db_table: str = 'persons'
        db_table_comment: str = 'Таблица содержит список людей'
        verbose_name: str = 'Человек'
        verbose_name_plural: str = 'Люди'
        ordering: Tuple[str] = ('id',)

    def __str__(self) -> str:
        """
        Метод возвращает полное имя

        Returns:
            str: Полное имя
        """
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    """Модель жанра"""

    title: models.CharField = models.CharField(max_length=255, verbose_name='Название')
    slug: models.SlugField = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    class Meta:
        db_table: str = 'genres'
        db_table_comment: str = 'Таблица содержит список жанров'
        verbose_name: str = 'Жанр'
        verbose_name_plural: str = 'Жанры'
        ordering: Tuple[str] = ('id',)

    def __str__(self) -> str:
        """
        Метод возвращает название жанра

        Returns:
            str: Название жанра
        """
        return str(self.title)


class Tag(models.Model):
    """Модель тега"""

    title: models.CharField = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        db_table: str = 'tags'
        db_table_comment: str = 'Таблица содержит список тегов'
        verbose_name: str = 'Тег'
        verbose_name_plural: str = 'Теги'
        ordering: Tuple[str] = ('id',)

    def __str__(self) -> str:
        """
        Метод возвращает название тега

        Returns:
            str: Название тега
        """
        return str(self.title)
