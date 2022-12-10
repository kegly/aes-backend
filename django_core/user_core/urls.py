from django.urls import path
from rest_framework import routers
from .views import StudentView
router = routers.DefaultRouter()
router.register(r'students', StudentView)
urlpatterns = []
urlpatterns += router.urls
