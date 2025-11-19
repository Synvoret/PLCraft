from django.contrib import admin


@admin.action(description="Copy selected with suffix (Copy)")
def copy(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None
        obj.name = f"{obj.name} (Copy)"
        obj.save()
