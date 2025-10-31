from django.shortcuts import render
from django.http import JsonResponse
from bagback.models import Bagpack


def bagpacks_view(request):
    bagpacks = Bagpack.objects.all()

    data = {}

    # return JsonResponse(data)
    return render(
        request,
        "bagpack/bagpack.html",
        {
            "bagpacks": bagpacks,
        },
    )
