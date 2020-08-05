from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import generics

from cart.serializers import UserSerializer, ItemSerializer
from cart.models import Item

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)


