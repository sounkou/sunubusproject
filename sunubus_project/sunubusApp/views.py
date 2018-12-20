from django.shortcuts import render
from rest_framework import generics
from .models import Heroes
from .models import Ligne
from .serializers import HeroesSerializer
from .serializers import LigneSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class HeroesList(generics.ListCreateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer

class HeroesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer 

class HeroesCreate(viewsets.ModelViewSet):
    queryset = Heroes.objects.all().order_by('-date_joined')
    serializer_class = HeroesSerializer
    
class LigneView(generics.ListCreateAPIView):
    queryset = Ligne.objects.all()
    serializer_class = LigneSerializer

      