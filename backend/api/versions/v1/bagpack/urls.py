from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.versions.v1.bagpack import BagpackViewSet

router = DefaultRouter()
router.register(r"", BagpackViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
