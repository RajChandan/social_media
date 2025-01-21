from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, login_user, logout_user, UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("", include(router.urls)),
]
