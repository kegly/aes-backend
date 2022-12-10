from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='teams')
urlpatterns += router.urls
