from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,
)
from .views import RegisterUserView, UserListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("logout/", TokenBlacklistView.as_view(), name="token-blacklist"),
    path("register/", RegisterUserView.as_view(), name="user-register"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
]
