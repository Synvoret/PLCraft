from django.contrib import admin
from bagback.models import Bagpack


@admin.register(Bagpack)
class BagpackAdmin(admin.ModelAdmin):
    list_display = ("name", "season", "type")
    list_filter = ("season", "type")
    search_fields = ("name", "type")
