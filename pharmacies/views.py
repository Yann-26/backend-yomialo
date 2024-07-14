from rest_framework import viewsets
from .models import *
from .serializers import  AssuranceSerializer, PharmacieSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny


def api_root(request):
    return render(request, 'api_root.html')


class AssuranceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer


class PharmaciesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer


