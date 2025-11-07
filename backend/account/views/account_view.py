from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class CustomLoginView(LoginView):
    template_name = "account/login.html"


class CustomLogoutView(LogoutView):
    template_name = "account/logout.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy(
        "welcome"
    )  # after registration, redirect to welcome page

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
