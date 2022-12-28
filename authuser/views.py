from django.shortcuts import render
from rest_framework import viewsets, permissions

from authuser.permissions import IsOwnerOrReadOnly
from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
