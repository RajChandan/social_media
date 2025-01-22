from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model

# {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3MjA5ODkzLCJpYXQiOjE3MzcyMDk1OTMsImp0aSI6IjFkYTA1M2E4NmQwNTQxNDE4YmQ1MzdmZGI0NzdhN2IzIiwidXNlcl9pZCI6Mn0.9xQnILOsZAG6QwL2RGJ8phYfOzZsQiBntA5ytip-oWw","refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzI5NTk5MywiaWF0IjoxNzM3MjA5NTkzLCJqdGkiOiI5YTAxYmI2Yzk3MzI0YmU4YTQwNDM0ZWNiNTEyNjgzNCIsInVzZXJfaWQiOjJ9.U94iyOlKTfF9Zd2xSkMayGPAGBSqvmwvWjMDMKArZMI"}

User = get_user_model()


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "user_registered succesfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                }
            )

        else:
            return Response(
                {"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    except User.DoesNotExist:
        return Response(
            {"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        token = request.data.get("refresh_token")
        token.blacklist()
        return Response(
            {"message": "User logged out successfuly"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["retrieve", "update", "partial_update", "profile", "follow"]:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def profile(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=["patch"], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Profile updated successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        user = request.user
        if user_to_follow == user:
            return Response(
                {"message": "you cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if user_to_follow in user.following.all():
            user.following.remove(user_to_follow)
            return Response(
                {"message": "you have unfollowed the user"}, status=status.HTTP_200_OK
            )
        else:
            user.following.add(user_to_follow)
            return Response(
                {"message": "you are now following the user"}, status=status.HTTP_200_OK
            )
