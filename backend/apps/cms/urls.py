from django.urls import path

from apps.cms.views.add_item import add_item
from apps.cms.views.collection import collection
from apps.cms.views.delete_item import delete_item
from apps.cms.views.edit_item import edit_item
from apps.cms.views.table import table

urlpatterns = [
    path("collection/", collection, name="collection"),
    path("table/", table, name="table"),
    path("table/add-item/", add_item, name="add-item"),
    path("table/edit-item/", edit_item, name="edit-item"),
    path("table/delete-item/", delete_item, name="delete-item"),
]
