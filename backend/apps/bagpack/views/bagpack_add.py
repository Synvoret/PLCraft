from django.contrib import messages
from django.shortcuts import redirect, render

from apps.bagpack.forms import BagpackForm


def bagpack_add(request):
    if not request.user.is_superuser:
        messages.warning(request, "You are not authorized to add bagpacks.")
        return redirect("bagpacks")

    if request.method == "POST":
        form = BagpackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Bagpack was added successfully.")
            return redirect("bagpacks")
    else:
        form = BagpackForm()
    return render(request, "bagpack/bagpack_add.html", {"form": form})
