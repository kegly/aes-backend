from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TagViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tags')
urlpatterns += router.urls
