from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins

from .models import *
from .serializers import *

# Create your views here.
class UserDetailAPIView(RetrieveAPIView):
    
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)
    
class UserViewSet(GenericViewSet, mixins.CreateModelMixin, ):
    def get_queryset(self):
        if self.action == 'retrieve':
            return User.objects.get(id=self.request.user.id)
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UserRetrieveSerializer
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)