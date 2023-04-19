from rest_framework import serializers
from .models import User, Box


class UserSerializer(serializers.ModelSerializer):
    boxes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='pk'
    )
    class Meta:
        model = User
        read_only_fields = ['id',]
        fields = ['first_name', 'last_name', 'email', 'password']

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        read_only_fields = ['id', 'volume', 'area']
        fields = '__all__'