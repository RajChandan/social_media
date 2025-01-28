from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post,Comment
from .serializers import CommentSerializer,PostSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({"message": "Post liked"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            comments = CommentSerializer(post.comments.all(), many=True).data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)