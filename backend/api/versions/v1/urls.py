from django.urls import include, path

urlpatterns = [
    path(f"accounts/", include("api.versions.v1.account.urls")),
    path(f"bagpacks/", include("api.versions.v1.bagpack.urls")),
    path(f"crochets/", include("api.versions.v1.crochet.urls")),
]
