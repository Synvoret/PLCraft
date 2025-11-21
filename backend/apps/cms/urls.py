from django.urls import path

from apps.cms.views.collection_view import collection_view
from apps.cms.views.get_collection_table import get_collection_table

urlpatterns = [
    path("collection/", collection_view, name="collection-view"),
    path("get-collection-table/", get_collection_table, name="get-collection-table"),
]
