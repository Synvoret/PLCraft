from django.urls import path, include

urlpatterns = [
    path("bagpacks/", include("api.versions.v1.bagpack.urls")),
    path("crochets/", include("api.versions.v1.crochet.urls")),
]
