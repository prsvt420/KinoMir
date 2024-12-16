import os
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
