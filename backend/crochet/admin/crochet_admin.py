from django.contrib import admin
from crochet.models import Crochet


@admin.register(Crochet)
class CrochetAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "type")
    list_filter = ("category", "type")
    search_fields = ("name", "category", "type")
