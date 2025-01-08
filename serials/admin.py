from typing import Tuple, Dict

from django.contrib import admin

from serials.models import Serial, SerialParticipant


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    """Админка сериалов"""

    list_display: Tuple = ('title', 'year', 'season_count', 'country', 'age_limit')
    list_filter: Tuple = ('country', 'age_limit', 'year')
    list_per_page: int = 50
    search_fields: Tuple = ('title', 'description')
    prepopulated_fields: Dict = {"slug": ("title",)}


@admin.register(SerialParticipant)
class SerialParticipantAdmin(admin.ModelAdmin):
    """Админка участников сериала"""

    list_display: Tuple = ('serial', 'person', 'role')
    list_per_page: int = 50
