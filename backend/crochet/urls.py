from django.urls import path
from .views import crochets_view


urlpatterns = [
    path("crochets", crochets_view, name="crochets"),
]
