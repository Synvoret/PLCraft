from django.urls import include, path

from api.utils import AllUrlsView, get_latest_api_version, schema_view

actual_api_version = get_latest_api_version()

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
