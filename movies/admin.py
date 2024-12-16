from typing import Tuple, Dict

from django.contrib import admin

from movies.models import Genre, Movie, Tag, FilmParticipant


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = ('title', 'slug')
    prepopulated_fields: Dict = {"slug": ("title",)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = ('title', 'year', 'duration', 'country', 'age_limit')
    list_filter: Tuple[str] = ('country', 'age_limit', 'year')
    list_per_page: int = 50
    search_fields: Tuple[str] = ('title', 'description')
    prepopulated_fields: Dict = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = ('title',)
    list_per_page: int = 50


@admin.register(FilmParticipant)
class FilmParticipantAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = ('movie', 'person', 'role')
    list_per_page: int = 50