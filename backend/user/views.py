from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"user_registered succesfully"},status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({'access_token':str(refresh.access_token),'refresh_token':str(refresh)})

        else:
            return Response({'error':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'error':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)


