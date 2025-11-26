import json

from django.http import JsonResponse
from django.template.loader import render_to_string

from apps.bagpack.models import Bagpack
from apps.crochet.models import Crochet


def add_item(request):
    if request.method == "POST":
        collection_type = request.POST.get("collection_type")
        if collection_type == "bagpack":
            model = Bagpack
        elif collection_type == "crochet":
            model = Crochet
        else:
            return JsonResponse({"ok": False, "html": "Unknown collection type."})

        exclude_fields = ["id", "created_at"]
        fields = [
            f.name
            for f in model._meta.get_fields()
            if f.concrete and not f.many_to_many and f.name not in exclude_fields
        ]

        data = {field: request.POST.get(field) for field in fields}
        model.objects.create(**data)

        items = model.objects.values(*fields, "id")
        fields_json = json.dumps(fields)

        html = render_to_string(
            "cms/collection_table.html",
            {
                "items": items,
                "fields": fields,
                "fields_json": fields_json,
                "collection_type": collection_type,
            },
        )

        return JsonResponse({"ok": True, "html": html})
