from rest_framework.routers import DefaultRouter

from .views import RatingViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'ratings', RatingViewSet, basename='ratings')
urlpatterns += router.urls
