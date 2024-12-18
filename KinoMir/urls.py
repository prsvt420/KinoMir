from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns: List = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls', namespace='movies'), name='movies'),
    path('serials/', include('serials.urls', namespace='serials'), name='serials'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += debug_toolbar_urls()
