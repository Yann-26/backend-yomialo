from django.shortcuts import render
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
