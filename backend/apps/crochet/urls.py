from django.urls import path

from apps.crochet.views import crochets_view

urlpatterns = [
    path("crochets/", crochets_view, name="crochets"),
]
