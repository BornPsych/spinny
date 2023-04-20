from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Box
from rest_framework import generics, permissions, status
from .serializers import UserSerializer, BoxSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .permission import IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.conf import settings
from .utils import manuallyValidate


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class createBoxView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    
    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            l, b, h = serializer.validated_data['length'], serializer.validated_data['breadth'], serializer.validated_data['height']
            area = l*b
            volume = l*b*h
            flag, message = manuallyValidate(request.user, area, volume)
            if flag:
                serializer.validated_data['created_by'] = request.user
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'error': message}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'not a staff user'}, status=status.HTTP_401_UNAUTHORIZED)

class BoxView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_field = "pk"

class BoxListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BoxSerializer

    def get_queryset(self):
        queryset = Box.objects.all()
        length_more_than = self.request.query_params.get('length_more_than')
        if length_more_than:
            queryset = queryset.filter(length__gte=length_more_than)

        length_less_than = self.request.query_params.get('length_less_than')
        if length_less_than:
            queryset = queryset.filter(length__lte=length_less_than)

        breadth_more_than = self.request.query_params.get('breadth_more_than')
        if breadth_more_than:
            queryset = queryset.filter(breadth__gte=breadth_more_than)

        breadth_less_than = self.request.query_params.get('breadth_less_than')
        if breadth_less_than:
            queryset = queryset.filter(breadth__lte=breadth_less_than)

        height_more_than = self.request.query_params.get('height_more_than')
        if height_more_than:
            queryset = queryset.filter(height__gte=height_more_than)

        height_less_than = self.request.query_params.get('height_less_than')
        if height_less_than:
            queryset = queryset.filter(height__lte=height_less_than)

        area_more_than = self.request.query_params.get('area_more_than')
        if area_more_than:
            queryset = queryset.filter(area__gte=area_more_than)

        area_less_than = self.request.query_params.get('area_less_than')
        if area_less_than:
            queryset = queryset.filter(area__lte=area_less_than)

        volume_more_than = self.request.query_params.get('volume_more_than')
        if volume_more_than:
            queryset = queryset.filter(volume__gte=volume_more_than)

        volume_less_than = self.request.query_params.get('volume_less_than')
        if volume_less_than:
            queryset = queryset.filter(volume__lte=volume_less_than)

        created_by = self.request.query_params.get('created_by')
        if created_by:
            queryset = queryset.filter(created_by=User.objects.get(id=created_by))

        created_before = self.request.query_params.get('created_before')
        if created_before:
            queryset = queryset.filter(created_at__lte=created_before)

        created_after = self.request.query_params.get('created_after')
        if created_after:
            queryset = queryset.filter(created_at__gte=created_after)

        return queryset


    

class UserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"


class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BoxSerializer

    def get_queryset(self):
        queryset = Box.objects.filter(created_by=self.request.user)

        length_more_than = self.request.query_params.get('length_more_than')
        if length_more_than:
            queryset = queryset.filter(length__gte=length_more_than)

        length_less_than = self.request.query_params.get('length_less_than')
        if length_less_than:
            queryset = queryset.filter(length__lte=length_less_than)

        breadth_more_than = self.request.query_params.get('breadth_more_than')
        if breadth_more_than:
            queryset = queryset.filter(breadth__gte=breadth_more_than)

        breadth_less_than = self.request.query_params.get('breadth_less_than')
        if breadth_less_than:
            queryset = queryset.filter(breadth__lte=breadth_less_than)

        height_more_than = self.request.query_params.get('height_more_than')
        if height_more_than:
            queryset = queryset.filter(height__gte=height_more_than)

        height_less_than = self.request.query_params.get('height_less_than')
        if height_less_than:
            queryset = queryset.filter(height__lte=height_less_than)

        area_more_than = self.request.query_params.get('area_more_than')
        if area_more_than:
            queryset = queryset.filter(area__gte=area_more_than)

        area_less_than = self.request.query_params.get('area_less_than')
        if area_less_than:
            queryset = queryset.filter(area__lte=area_less_than)

        volume_more_than = self.request.query_params.get('volume_more_than')
        if volume_more_than:
            queryset = queryset.filter(volume__gte=volume_more_than)

        volume_less_than = self.request.query_params.get('volume_less_than')
        if volume_less_than:
            queryset = queryset.filter(volume__lte=volume_less_than)

        return queryset