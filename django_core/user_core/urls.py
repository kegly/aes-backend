from django.urls import path
from rest_framework import routers
from .views import StudentView, CompanyView

router = routers.DefaultRouter()
router.register(r'students', StudentView)
router.register(r'companies', CompanyView)
urlpatterns = []
urlpatterns += router.urls
