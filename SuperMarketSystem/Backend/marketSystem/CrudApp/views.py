from django.shortcuts import render

from .models import SuperMarketSystem
from .serializers import SuperMarketSerializer
from rest_framework import status
from rest_framework import viewsets


# Create your views here.
class SuperMarketDataSystem(viewsets.ModelViewSet):
    queryset=SuperMarketSystem.objects.all()
    serializer_class=SuperMarketSerializer