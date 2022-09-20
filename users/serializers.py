from rest_framework.serializers import ModelSerializer
from .models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'two_factor',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

