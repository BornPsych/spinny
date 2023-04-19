from rest_framework import serializers
from .models import User, Box


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['id',]
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        read_only_fields = ['id',]
        fields = '__all__'