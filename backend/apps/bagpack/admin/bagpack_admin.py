from django.contrib import admin

from apps.bagpack.models import Bagpack


@admin.action(description="Copy selected")
def copy(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None
        obj.save()

@admin.register(Bagpack)
class BagpackAdmin(admin.ModelAdmin):
    list_display = ("name", "season", "type", "created_at")
    list_filter = ("season", "type", "created_at")
    search_fields = ("name", "type")
    actions = [copy]
