from rest_framework.serializers import ModelSerializer
from .models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'last_pass_change',
            'auth_token',
        ]
