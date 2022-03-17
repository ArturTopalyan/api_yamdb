from django.conf.urls import include
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genres')