from rest_framework import serializers
from .models import Post,Comment
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = Comment
        fields = ["id","author","content","created_at"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ["id","author","content","image","created_at","like_count","comments"]
