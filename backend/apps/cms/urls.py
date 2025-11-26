from django.urls import path

from apps.cms.views.add_item import add_item
from apps.cms.views.collection_table import collection_table
from apps.cms.views.collection_view import collection_view
from apps.cms.views.delete_item import delete_item

urlpatterns = [
    path("collection/", collection_view, name="collection-view"),
    path("collection-table/", collection_table, name="collection-table"),
    path("collection-table/add-item", add_item, name="add-item"),
    path("collection-table/delete-item", delete_item, name="delete-item"),
]
