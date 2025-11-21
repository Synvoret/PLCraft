from django.urls import path

from apps.account.views import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    # ACCOUNTs
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
