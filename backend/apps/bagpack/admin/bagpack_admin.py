from django.contrib import admin

from apps.bagpack.models import Bagpack


@admin.action(description="Set season to Spring")
def set_season_spring(modeladmin, request, queryset):
    queryset.update(season="spring")


@admin.action(description="Set season to Summer")
def set_season_summer(modeladmin, request, queryset):
    queryset.update(season="summer")


@admin.action(description="Set season to Autumn")
def set_season_autumn(modeladmin, request, queryset):
    queryset.update(season="Autumn")


@admin.action(description="Set season to Winter")
def set_season_winter(modeladmin, request, queryset):
    queryset.update(season="winter")


@admin.register(Bagpack)
class BagpackAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = ("name", "season", "type", "created_at")
    list_filter = ("season", "type", "created_at")
    search_fields = ("name", "type")
    actions = [
        set_season_spring,
        set_season_summer,
        set_season_autumn,
        set_season_winter,
    ]
