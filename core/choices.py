from django.db import models


class RoleChoices(models.TextChoices):
    """Класс с ролями"""

    ACTOR = 'actor', 'Актёр'
    DIRECTOR = 'director', 'Режиссёр'
    PRODUCER = 'producer', 'Продюсер'
    SCREENWRITER = 'screenwriter', 'Сценарист'
    OPERATOR = 'operator', 'Оператор'
