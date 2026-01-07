import json

from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string

from apps.bagpack.models import Bagpack
from apps.cms.forms import BagpackForm, CrochetForm
from apps.crochet.models import Crochet


def edit_item(request):
    collection_type = request.GET.get("collection_type") or request.POST.get(
        "collection_type"
    )
    pk = request.GET.get("id") or request.POST.get("id")

    if not collection_type or not pk:
        return JsonResponse(
            {"ok": False, "html": "No collection type or id."}, status=400
        )

    if collection_type == "bagpack":
        form_class = BagpackForm
        model = Bagpack
    elif collection_type == "crochet":
        form_class = CrochetForm
        model = Crochet
    else:
        return JsonResponse(
            {"ok": False, "html": "Unknown collection type."}, status=400
        )

    try:
        instance = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return JsonResponse({"ok": False, "html": "Element doesn't exist."}, status=404)

    if request.method == "GET":
        form = form_class(instance=instance)
        html = render_to_string(
            "cms/table/_table_edit_form.html",
            {
                "form": form,
                "item": instance,
                "collection_type": collection_type,
            },
        )
        return JsonResponse({"ok": True, "html": html})

    if request.method == "POST":
        # Zapis edycji
        form = form_class(request.POST, request.FILES, instance=instance)
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

    return JsonResponse({"ok": False, "html": "Method not allowed."}, status=405)
