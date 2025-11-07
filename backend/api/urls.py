from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.utils import get_latest_api_version
from api.utils import AllUrlsView

actual_api_version = get_latest_api_version()

schema_view = get_schema_view(
    openapi.Info(
        title="PLCraft API",
        default_version=actual_api_version,
        description=f"API documentation for PLCraft project - version {actual_api_version}",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path(
        f"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        f"redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    # API version
    path(f"", include(f"api.versions.{actual_api_version}.urls")),
    path(f"all-urls/", AllUrlsView.as_view(), name="all-urls"),
]
