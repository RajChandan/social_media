from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import register_user

router = DefaultRouter()
router.register(r'user',)