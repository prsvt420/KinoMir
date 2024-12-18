from typing import Tuple

from django.db import models
from django.urls import reverse

from core.choices import RoleChoices
from core.models import Person, Tag, Genre


class Movie(models.Model):
    """Модель фильма"""

    title: models.CharField = models.CharField(max_length=255, verbose_name='Название', )
    description: models.TextField = models.TextField(verbose_name='Описание')
    poster: models.ImageField = models.ImageField(
        upload_to='movies/',
        verbose_name='Постер',
        help_text='Рекомендуемый размер 300x450',
    )
    year: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Год')
    duration: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Продолжительность', )
    country: models.CharField = models.CharField(max_length=255, verbose_name='Страна')
    age_limit: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Возрастное ограничение')
    genres: models.ManyToManyField = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
    )
    tags: models.ManyToManyField = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        blank=True,
    )
    slug: models.SlugField = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    class Meta:
        db_table: str = 'movies'
        db_table_comment: str = 'Таблица содержит список фильмов'
        verbose_name: str = 'Фильм'
        verbose_name_plural: str = 'Фильмы'
        ordering: Tuple[str] = ('id',)

    def __str__(self) -> str:
        """
        Метод возвращает название фильма

        Returns:
            str: Название фильма
        """
        return str(self.title)

    def get_absolute_url(self) -> str:
        """Метод возвращает абсолютный URL конкретного фильма"""
        return reverse('movies:movie-detail', kwargs={'slug': self.slug})

    def get_duration(self) -> str:
        """Метод возвращает продолжительность фильма"""
        return f'{self.duration // 60} ч {self.duration % 60} мин'


class FilmParticipant(models.Model):
    """Связывающая модель между фильмом и человеком с указанием роли"""

    movie: models.ForeignKey = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        verbose_name='Фильм',
    )
    person: models.ForeignKey = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Человек',
    )
    role: models.CharField = models.CharField(max_length=50, choices=RoleChoices.choices, verbose_name='Роль')

    class Meta:
        db_table: str = 'film_participants'
        db_table_comment: str = 'Таблица содержит список членов фильма'
        verbose_name: str = 'Член фильма'
        verbose_name_plural: str = 'Члены фильма'
        ordering: Tuple[str] = ('id',)
        unique_together: Tuple[str] = ('movie', 'person')
