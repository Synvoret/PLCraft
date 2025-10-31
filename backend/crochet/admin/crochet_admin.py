from django.contrib import admin
from crochet.models import Crochet


@admin.register(Crochet)
class CrochetAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("type",)
    search_fields = ("name",)
