from django.urls import path
from api.versions.v1.bagpack import BagpackView, BackpackDetailView
from api.versions.v1.crochet import CrochetView, CrochetDetailView

urlpatterns = [
    path("bagpacks/", BagpackView.as_view(), name="bagpack-list"),
    path("bagpacks/<int:pk>/", BackpackDetailView.as_view(), name="bagpack-detail"),
    path("crochets/", CrochetView.as_view(), name="crochet-list"),
    path("crochets/<int:pk>/", CrochetDetailView.as_view(), name="crochet-detail"),
]
