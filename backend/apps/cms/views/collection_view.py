from django.contrib import messages
from django.shortcuts import redirect, render

from apps.cms.forms import BagpackForm, CollectionForm

# def collection_view(request):
#     if not request.user.is_superuser:
#         messages.warning(request, "You are not authorized to view collection.")
#         return redirect("welcome")

# if request.method == "POST":
#     form = BagpackForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Bagpack was added successfully.")
#         return redirect("bagpacks")
# else:
#     form = BagpackForm()
# return render(request, "cms/collection.html", {"form": form})
# return render(request, "cms/collection.html")


def collection_view(request):
    if not request.user.is_superuser:
        messages.warning(request, "You are not authorized to view collection.")
        return redirect("welcome")
    form = CollectionForm()
    return render(request, "cms/collection.html", {"form": form})
