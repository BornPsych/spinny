from django.shortcuts import render
from django.http import JsonResponse
from .models import user1
from rest_framework import generics
from .serializers import UserSerializer

"""Create your views here.
def index(request):
    return JsonResponse({'foo':'bar'})

def model_view(request, pk):
    try:
        data = user1.objects.get(pk=pk)
        res = {
            'first_name': data.firstName,
        }
        return JsonResponse(res)
    except Exception as e:
        print(e)
        return JsonResponse({'error':'user1 with this pk not found'})
"""

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = user1.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class createUserView(generics.CreateAPIView):
    queryset = user1.objects.all()
    serializer_class = UserSerializer
