from django.urls import URLPattern, URLResolver, get_resolver
from rest_framework import generics, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser


class UrlSerializer(serializers.Serializer):
    path = serializers.CharField()
    name = serializers.CharField()
    view = serializers.CharField()
    full_url = serializers.CharField()


class UrlPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 100


class AllUrlsView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UrlSerializer
    pagination_class = UrlPagination

    def get_queryset(self):
        resolver = get_resolver()
        urls = []
        self.request.build_absolute_uri("/")

        def list_urls(patterns, prefix=""):
            for pattern in patterns:
                if isinstance(pattern, URLPattern):
                    path_str = prefix + str(pattern.pattern)
                    urls.append(
                        {
                            "path": path_str,
                            "name": pattern.name or "",
                            "view": f"{pattern.callback.__module__}.{pattern.callback.__name__}",
                            "full_url": "/" + path_str.lstrip("/"),
                        }
                    )
                elif isinstance(pattern, URLResolver):
                    list_urls(pattern.url_patterns, prefix + str(pattern.pattern))

        list_urls(resolver.url_patterns)
        urls.sort(key=lambda x: x["path"])
        return urls

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        return self.get_paginated_response(page)
