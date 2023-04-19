from rest_framework import serializers
from .models import user1, action


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user1
        read_only_fields = ['id',]
        fields = '__all__'