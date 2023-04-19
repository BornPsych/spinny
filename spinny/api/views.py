from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Box
from rest_framework import generics
from .serializers import UserSerializer, BoxSerializer
# Create your views here.

class createBoxView(generics.CreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_field = "pk"

class BoxListView(generics.ListAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.filter(created_by=request.user)
    serializer_class = UserSerializer
    lookup_field = "Fi"