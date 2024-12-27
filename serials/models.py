from typing import Tuple, Optional

from django.db import models
from django.urls import reverse

from core.choices import RoleChoices
from core.models import Person, Tag, Genre


class Serial(models.Model):
    """Модель сериала"""

    title: models.CharField = models.CharField(max_length=255, verbose_name='Название', )
    description: models.TextField = models.TextField(verbose_name='Описание')
    poster: models.ImageField = models.ImageField(
        upload_to='serials/',
        verbose_name='Постер',
        help_text='Рекомендуемый размер 300x450',
    )
    year: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Год')
    season_count: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Количество сезонов')
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
        db_table: str = 'serials'
        db_table_comment: str = 'Таблица содержит список сериалов'
        verbose_name: str = 'Сериал'
        verbose_name_plural: str = 'Сериалы'
        ordering: Tuple[str] = ('id',)

    def __str__(self) -> str:
        """
        Метод возвращает название сериала

        Returns:
            str: Название сериала
        """
        return str(self.title)

    def get_absolute_url(self) -> str:
        """Метод возвращает абсолютный URL конкретного сериала"""
        return reverse('serials:serial-detail', kwargs={'slug': self.slug})

    def get_season_count(self) -> str:
        """Метод возвращает количество сезонов сериала"""

        end_word: Optional[str] = None

        if str(self.season_count)[-1] == '1':
            end_word = ''
        elif str(self.season_count)[-1] in '234':
            end_word = 'а'
        else:
            end_word = 'ов'

        return f'{self.season_count} сезон{end_word}'


class SerialParticipant(models.Model):
    """Связывающая модель между сериалом и человеком с указанием роли"""

    serial: models.ForeignKey = models.ForeignKey(
        'Serial',
        on_delete=models.CASCADE,
        verbose_name='Сериал',
    )
    person: models.ForeignKey = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Человек',
    )
    role: models.CharField = models.CharField(max_length=50, choices=RoleChoices.choices, verbose_name='Роль')

    class Meta:
        db_table: str = 'serial_participants'
        db_table_comment: str = 'Таблица содержит список членов сериала'
        verbose_name: str = 'Член сериала'
        verbose_name_plural: str = 'Члены сериала'
        ordering: Tuple = ('id',)
        unique_together: Tuple = ('serial', 'person')
