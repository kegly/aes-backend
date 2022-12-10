from django.urls import path
from rest_framework import routers
from .views import CVView, CVFilterViewSet

router = routers.DefaultRouter()
router.register(r'cv', CVView)
router.register(r'cv_filter', CVFilterViewSet)
urlpatterns = []
urlpatterns += router.urls
