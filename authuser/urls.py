from django.urls import path, include
from rest_framework import routers

from authuser.views import UserViewSet, UserRegisterViewset, LoginViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet, basename="user")
router.register("register", UserRegisterViewset, basename="register")
router.register("login", LoginViewSet, basename="login")


urlpatterns = [
    path("", include(router.urls)),
]
