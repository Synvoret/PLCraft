from django.urls import path

from apps.bagpack.views import bagpacks_view

urlpatterns = [
    path("bagpacks/", bagpacks_view, name="bagpacks"),
]
