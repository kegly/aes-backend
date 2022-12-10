from django.urls import path
from rest_framework import routers
from .views import ApplicationView, ApplicationsFilterViewSet

router = routers.DefaultRouter()
router.register(r'application', ApplicationView)
router.register(r'application_filter', ApplicationsFilterViewSet)
urlpatterns = []
urlpatterns += router.urls
