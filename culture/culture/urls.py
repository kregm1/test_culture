from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import TheatreViewSet, SearchView


router = DefaultRouter()
router.register(r'theatre', TheatreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', SearchView.as_view(), name='search'),
    path('', include(router.urls)),
]
