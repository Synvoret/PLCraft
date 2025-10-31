from django.contrib import admin
from bagback.models import Bagpack


@admin.register(Bagpack)
class BagpackAdmin(admin.ModelAdmin):
    list_display = ("name", "season")
    list_filter = ("season",)
    search_fields = ("name",)
