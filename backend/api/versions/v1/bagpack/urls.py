from django.urls import path
from api.versions.v1.bagpack import (
    BagpackListView,
    BagpackCreateView,
    BagpackDetailView,
    BagpackUpdateView,
    BagpackDeleteView,
)

urlpatterns = [
    path("", BagpackListView.as_view(), name="bagpack-list"),
    path("create/", BagpackCreateView.as_view(), name="bagpack-create"),
    path("<int:pk>/detail/", BagpackDetailView.as_view(), name="bagpack-detail"),
    path("<int:pk>/update/", BagpackUpdateView.as_view(), name="bagpack-update"),
    path("<int:pk>/delete/", BagpackDeleteView.as_view(), name="bagpack-delete"),
]
