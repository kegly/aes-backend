from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer, UserDeleteSerializer

User = get_user_model()


class BaseUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class BaseUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = '__all__'
