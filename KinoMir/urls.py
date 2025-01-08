from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns: List = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core"), name="core"),
    path("movies/", include("movies.urls", namespace="movies"), name="movies"),
    path("serials/", include("serials.urls", namespace="serials"), name="serials"),
    path("api/", include("api.urls", namespace="api"), name="api"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += debug_toolbar_urls()
