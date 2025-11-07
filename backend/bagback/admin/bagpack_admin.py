from django.contrib import admin
from bagback.models import Bagpack


@admin.register(Bagpack)
class BagpackAdmin(admin.ModelAdmin):
    list_display = ("name", "season", "type", "created_at")
    list_filter = ("season", "type", "created_at")
    search_fields = ("name", "type")
