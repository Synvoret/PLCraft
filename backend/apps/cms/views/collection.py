from django.contrib import messages
from django.shortcuts import redirect, render

from apps.cms.forms import CollectionForm


def collection(request):
    if not request.user.is_superuser:
        messages.warning(request, "You are not authorized to view collection.")
        return redirect("welcome")
    form = CollectionForm()
    return render(request, "cms/collection.html", {"form": form})
