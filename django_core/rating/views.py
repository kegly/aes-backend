from rest_framework.viewsets import ModelViewSet

from .models import Rating

from .serializers import RatingSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    