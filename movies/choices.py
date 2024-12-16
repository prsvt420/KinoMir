from typing import Tuple

from django.db import models


class RoleChoices(models.TextChoices):
    ACTOR: Tuple = 'actor', 'Актёр'
    DIRECTOR: Tuple = 'director', 'Режиссёр'
    PRODUCER: Tuple = 'producer', 'Продюсер'
    SCREENWRITER: Tuple = 'screenwriter', 'Сценарист'
    OPERATOR: Tuple = 'operator', 'Оператор'
