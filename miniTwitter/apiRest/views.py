from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsuarioSerializer, PostSerializer
from .models import Usuario, Post


class UsarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('name')
    serializer_class = UsuarioSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

