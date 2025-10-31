from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .utils import get_latest_api_version

# Actual API version
actual_api_version = get_latest_api_version()

schema_view = get_schema_view(
    openapi.Info(
        title="PLCraft API",
        default_version=actual_api_version,
        description="API documentation for PLCraft project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger UI path
    path(
        f"{actual_api_version}/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # API version
    path(f"{actual_api_version}/", include(f"api.versions.{actual_api_version}.urls")),
]
