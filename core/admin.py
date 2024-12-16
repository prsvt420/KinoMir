from typing import Tuple

from django.contrib import admin

from core.models import Person


@admin.register(Person)
class FilmParticipantAdmin(admin.ModelAdmin):
    fields: Tuple[str] = (
        ('first_name', 'last_name'),
        'photo'
    )

    list_display: Tuple[str] = (
        'first_name',
        'last_name',
    )

    search_fields: Tuple[str] = (
        'first_name',
        'last_name',
    )

    list_per_page: int = 50
