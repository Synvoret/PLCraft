from django.shortcuts import render
from apps.crochet.models import Crochet


def crochets_view(request):
    select_single_crochets = Crochet.objects.filter(type="single").order_by("?")

    context = {
        "crochets": select_single_crochets,
    }

    return render(
        request,
        "crochet/crochet.html",
        context=context,
    )
