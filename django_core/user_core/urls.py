from django.urls import path
from rest_framework import routers
from .views import StudentView, CompanyView, HRView

router = routers.DefaultRouter()
router.register(r'students', StudentView)
router.register(r'companies', CompanyView)
router.register(r'hrs', HRView)
urlpatterns = []
urlpatterns += router.urls
