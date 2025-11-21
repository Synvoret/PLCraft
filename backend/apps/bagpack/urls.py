from django.urls import path

from .views import bagpack_add, bagpacks_view

urlpatterns = [
    path("bagpacks/", bagpacks_view, name="bagpacks"),
    path("bagpack-add/", bagpack_add, name="bagpack-add"),
]
