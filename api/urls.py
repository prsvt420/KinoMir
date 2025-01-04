from typing import List

from django.urls import path, include
from rest_framework import routers
from .yasg import urlpatterns as yasg_urls
from api.views import MovieViewSet, SerialViewSet

app_name: str = 'api'

router: routers.DefaultRouter = routers.DefaultRouter()

router.register(prefix=r'movies', viewset=MovieViewSet, basename='movies')
router.register(prefix=r'serials', viewset=SerialViewSet, basename='serials')

urlpatterns: List = [
    path('', include(router.urls)),
]

urlpatterns += yasg_urls
