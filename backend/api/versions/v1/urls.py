from django.urls import path
from api.versions.v1.bagpack import (
    BagpackListView,
    BagpackCreateView,
    BagpackDetailView,
    BagpackUpdateView,
    BagpackDeleteView,
)
from api.versions.v1.crochet import CrochetView, CrochetDetailView

urlpatterns = [
    path("bagpacks/", BagpackListView.as_view(), name="bagpack-list"),
    path(
        "bagpacks/<int:pk>/create/", BagpackCreateView.as_view(), name="bagpack-create"
    ),
    path(
        "bagpacks/<int:pk>/detail/", BagpackDetailView.as_view(), name="bagpack-detail"
    ),
    path(
        "bagpacks/<int:pk>/update/", BagpackUpdateView.as_view(), name="bagpack-update"
    ),
    path(
        "bagpacks/<int:pk>/delete/", BagpackDeleteView.as_view(), name="bagpack-delete"
    ),
    path("crochets/", CrochetView.as_view(), name="crochet-list"),
    path("crochets/<int:pk>/", CrochetDetailView.as_view(), name="crochet-detail"),
]
