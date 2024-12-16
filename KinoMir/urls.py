from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from core.views import redirect_to_movies

urlpatterns: List = [
    path('admin/', admin.site.urls),
    re_path(r'^$', redirect_to_movies, name='redirect-to-movies'),
    path('movies/', include('movies.urls', namespace='movies'), name='movies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
