from rest_framework import serializers, permissions

from .models import User, Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        read_only_fields = ['id', 'area','volume', 'created_by','created_at']
        fields = '__all__'
    
    
    def get_fields(self, *args, **kwargs):
        fields = super(BoxSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and request.user.is_staff:
            return fields
        else:
            # Remove certain fields if the user is not staff
            fields.pop('created_by', None)
            fields.pop('created_at', None)
            return fields

class UserSerializer(serializers.ModelSerializer):
    boxes = BoxSerializer(read_only=True, many=True)

    class Meta:
        model = User
        read_only_fields = ['id']
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'boxes']
        extra_kwargs = {
            'password': {'write_only': True}
        }