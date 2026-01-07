import json

from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string

from apps.bagpack.models import Bagpack
from apps.cms.forms import BagpackForm, CrochetForm
from apps.crochet.models import Crochet


def add_item(request):
    collection_type = request.GET.get("collection_type") or request.POST.get(
        "collection_type"
    )

    if collection_type == "bagpack":
        form_class = BagpackForm
        model = Bagpack
    elif collection_type == "crochet":
        form_class = CrochetForm
        model = Crochet
    else:
        return JsonResponse({"ok": False, "html": "Unknown collection type."})

    if request.method == "GET":
        form = form_class()
        html = render_to_string("cms/table/_table_add_form.html", {"form": form})
        return JsonResponse({"ok": True, "html": html})

    if request.method == "POST":

        collection_type = request.POST.get("collection_type")
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
        else:
            messages.warning(request, "Form is not valid. Please enter correct data.")
            msgs = [
                {"level": m.level, "message": m.message, "tags": m.tags}
                for m in messages.get_messages(request)
            ]
            return JsonResponse({"ok": False, "messages": msgs}, status=400)

        fields = [
            f.name
            for f in instance._meta.get_fields()
            if f.concrete and not f.many_to_many and f.name not in ["id", "created_at"]
        ]
        items = model.objects.values(*fields, "id")

        html = render_to_string(
            "cms/table/table.html",
            {
                "items": items,
                "fields": fields,
                "fields_json": json.dumps(fields),
                "collection_type": collection_type,
            },
        )
        return JsonResponse({"ok": True, "html": html})
