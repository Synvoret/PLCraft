from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.utils import get_latest_api_version

actual_api_version = get_latest_api_version()

schema_view = get_schema_view(
    openapi.Info(
        title="PLCraft API",
        default_version=actual_api_version,
        description=f"API documentation for PLCraft project - version {actual_api_version}",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    patterns=[path("", include(f"api.versions.{actual_api_version}.urls"))],
)
