from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class CreateUserAPIView(CreateAPIView):
    @swagger_auto_schema(tags=["User"])
    def post(self, request, *args, **kwargs):
        user_name