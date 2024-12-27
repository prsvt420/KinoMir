from typing import Tuple, Dict

from django.contrib import admin

from core.models import Person, Tag, Genre


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Админка персон"""

    fields: Tuple = (
        ('first_name', 'last_name'),
        'photo'
    )

    list_display: Tuple = (
        'first_name',
        'last_name',
    )

    search_fields: Tuple= (
        'first_name',
        'last_name',
    )

    list_per_page: int = 50


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Админка тегов"""

    list_display: Tuple = ('title',)
    list_per_page: int = 50


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Админка жанров"""

    list_display: Tuple = ('title', 'slug')
    prepopulated_fields: Dict = {"slug": ("title",)}
