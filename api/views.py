from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ApiSerializer
from .models import Post
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ApiSerializer