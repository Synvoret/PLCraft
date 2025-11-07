from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # Application paths
    path("", include("account.urls")),
    path("", include("welcome.urls")),
    path("", include("bagback.urls")),
    path("", include("crochet.urls")),
]

# Static and media files serving during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
