from django.urls import path

from api.versions.v1.crochet import (
    CrochetDeleteView,
    CrochetDetailView,
    CrochetListCreateView,
    CrochetUpdateView,
)

urlpatterns = [
    path("", CrochetListCreateView.as_view(), name="crochet-list-create"),
    path("<int:pk>/detail/", CrochetDetailView.as_view(), name="crochet-detail"),
    path("<int:pk>/update/", CrochetUpdateView.as_view(), name="crochet-update"),
    path("<int:pk>/delete/", CrochetDeleteView.as_view(), name="crochet-delete"),
]
