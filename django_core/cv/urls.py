from django.urls import path
from rest_framework import routers
from .views import CVView
router = routers.DefaultRouter()
router.register(r'cv', CVView)
urlpatterns = []
urlpatterns += router.urls
