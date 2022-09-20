from django.urls import path
from ..views.views_v_1 import UserCreateAPIView

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name="create_user")
]