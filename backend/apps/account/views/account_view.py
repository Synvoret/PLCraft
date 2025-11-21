from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class UserLoginView(LoginView):
    template_name = "account/login.html"

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in.")
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("welcome")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy("welcome")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(
            self.request, "Your account has been created and you are now logged in!"
        )
        return super().form_valid(form)
