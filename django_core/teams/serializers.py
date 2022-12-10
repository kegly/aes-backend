from rest_framework.serializers import ModelSerializer, ManyRelatedField, FloatField

from .models import Team


class TeamSerializer(ModelSerializer):
    rating = FloatField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
