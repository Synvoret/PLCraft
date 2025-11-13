from django.contrib import admin
from apps.crochet.models import Crochet


@admin.register(Crochet)
class CrochetAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "type", "created_at")
    list_filter = ("category", "type", "created_at")
    search_fields = ("name", "category", "type")
