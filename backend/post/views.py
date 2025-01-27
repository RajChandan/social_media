from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post,Comment
from .serializers import CommentSerializer,PostSerializer
# Create your views here.
