from ..models import User
from ..serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.validators import ValidationError

from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(tags=["User"])
    def post(self, request, *args, **kwargs):
        user_name = request.data.get('email', None)
        if user_name is None:
            raise ValidationError("Email is required")
        user_name = user_name.split('@')[0]
        request.data['username'] = user_name
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_obj = User.objects.create(
                username=user_name,
                email=request.data["email"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                two_factor=request.data["two_factor"]
            )
            user_obj.set_password(request.data["password"])
            user_obj.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

