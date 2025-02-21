from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    register_user,
    login_user,
    logout_user,
    UserViewSet,
    github_login,
    github_callback,
)

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("github/login/", github_login, name="github_login"),
    path("github/callback/", github_callback, name="github_callback"),
    path("", include(router.urls)),
]
