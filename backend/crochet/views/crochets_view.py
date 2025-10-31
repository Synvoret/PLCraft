import random
from django.shortcuts import render
from bagback.models import Bagpack
from crochet.models import Crochet


def crochets_view(request):
    # bagpacks = list(Bagpack.objects.all())
    # crochets = list(Crochet.objects.all())

    # select_bagpacks = random.sample(bagpacks, min(len(bagpacks), 3))
    # select_crochets = random.sample(crochets, min(len(crochets), 3))

    # context = {
    #     "bagpacks": select_bagpacks,
    #     "crochets": select_crochets,
    # }
    context = {}

    return render(request, "crochet/crochet.html", context)
