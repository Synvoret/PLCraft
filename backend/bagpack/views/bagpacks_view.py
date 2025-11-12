from django.shortcuts import render
from bagpack.models import Bagpack


def bagpacks_view(request):
    select_single_bagpacks = Bagpack.objects.filter(type="single").order_by("?")

    context = {
        "bagpacks": select_single_bagpacks,
    }

    return render(
        request,
        "bagpack/bagpack.html",
        context=context,
    )
