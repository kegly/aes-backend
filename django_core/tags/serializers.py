from rest_framework.serializers import ModelSerializer

from tags.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
