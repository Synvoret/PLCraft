from django.urls import path
from api.versions.v1.crochet import (
    CrochetListView,
    CrochetCreateView,
    CrochetDetailView,
    CrochetUpdateView,
    CrochetDeleteView,
)

urlpatterns = [
    path("", CrochetListView.as_view(), name="crochet-list"),
    path("create/", CrochetCreateView.as_view(), name="crochet-create"),
    path("<int:pk>/detail/", CrochetDetailView.as_view(), name="crochet-detail"),
    path("<int:pk>/update/", CrochetUpdateView.as_view(), name="crochet-update"),
    path("<int:pk>/delete/", CrochetDeleteView.as_view(), name="crochet-delete"),
]
