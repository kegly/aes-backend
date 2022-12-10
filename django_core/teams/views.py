from django.db.models import Avg, F
from rest_framework.viewsets import ModelViewSet

from .models import Team

from .serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(rating=Avg(F('ratings__rating')))
