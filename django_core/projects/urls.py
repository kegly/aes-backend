from django.urls import path
from rest_framework import routers
from .views import ProjectFilterViewSet, ProjectView

router = routers.DefaultRouter()
router.register(r'filter_projects', ProjectFilterViewSet)
router.register(r'projects', ProjectView)

urlpatterns = []
urlpatterns += router.urls
