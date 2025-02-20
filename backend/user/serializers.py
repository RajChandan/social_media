from importlib.metadata import requires


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    followers = serializers.StringRelatedField(many=True)
    following = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "bio",
            "profile_picture",
            "followers",
            "following",
            "followers_count",
            "following_count",
        ]

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()

    def get_profile_picture(self, obj):
        request = self.context.get("request")
        if obj.profile_picture:
            return request.build_absolute_uri(obj.profile_picture.url)
        return "https://avatar.iran.liara.run/public/boy"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    github_id = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
            "github_id",
        ]

    def create(self, validated_data):
        github_id = validated_data.pop("github_id", None)
        if github_id:
            user, created = User.objects.get_or_create(
                email=validated_data["email"],
                defaults={
                    "username": validated_data.get("username"),
                    "first_name": validated_data.get("first_name", ""),
                    "last_name": validated_data.get("last_name", ""),
                    "bio": validated_data.get("bio", ""),
                    "profile_picture": validated_data.get("profile_picture", None),
                },
            )

        else:
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
                first_name=validated_data.get("first_name", ""),
                last_name=validated_data.get("last_name", ""),
                bio=validated_data.get("bio", ""),
                profile_picture=validated_data.get("profile_picture", None),
            )

        return user
