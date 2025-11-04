from django.shortcuts import render
from bagback.models.bagpack_model import Bagpack
from crochet.models.crochet_model import Crochet


def welcome_view(request):

    select_multi_bagpacks = Bagpack.objects.filter(type="multi").order_by("?")[:3]
    select_multi_crochets = Crochet.objects.filter(type="multi").order_by("?")[:3]

    context = {
        "bagpacks": select_multi_bagpacks,
        "crochets": select_multi_crochets,
    }

    return render(request, "welcome/welcome.html", context)
