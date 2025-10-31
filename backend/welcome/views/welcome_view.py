import random
from django.shortcuts import render
from bagback.models.bagpack_model import Bagpack
from crochet.models.crochet_model import Crochet


def welcome_view(request):
    bagpacks = list(Bagpack.objects.all())
    crochets = list(Crochet.objects.all())

    select_bagpacks = random.sample(bagpacks, min(len(bagpacks), 9))
    select_crochets = random.sample(crochets, min(len(crochets), 3))

    context = {
        "bagpacks": select_bagpacks,
        "crochets": select_crochets,
    }
    print(context)

    return render(request, "welcome/welcome.html", context)
