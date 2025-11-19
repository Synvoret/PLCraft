from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"

    def ready(self):
        from django.contrib import admin

        from apps.common.admin_actions import copy

        admin.site.add_action(copy)
