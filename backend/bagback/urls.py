from django.urls import path
from .views import bagpacks_view


urlpatterns = [
    path("bagpacks", bagpacks_view, name="bagpacks"),
]
