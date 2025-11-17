from django.shortcuts import render

from apps.bagpack.models import Bagpack
from apps.crochet.models import Crochet


def welcome_view(request):

    select_multi_bagpacks = Bagpack.objects.filter(type="multi").order_by("?")[:5]
    select_multi_crochets = Crochet.objects.filter(type="multi").order_by("?")[:5]
    select_all_bagpacks = Bagpack.objects.all()

    context = {
        "bagpacks": select_all_bagpacks,
        "crochets": select_multi_crochets,
    }

    return render(request, "welcome/welcome.html", context)
