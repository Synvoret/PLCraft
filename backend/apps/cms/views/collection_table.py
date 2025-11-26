import json

from django.http import JsonResponse
from django.template.loader import render_to_string

from apps.cms.forms import COLLECTION_CHOICES
from apps.bagpack.models import Bagpack
from apps.crochet.models import Crochet


def collection_table(request):
    collection_type = request.GET.get("collection_type")
    
    if collection_type == 'bagpack':
        model = Bagpack
    elif collection_type == 'crochet':
        model = Crochet
    else:
        return JsonResponse({"ok": False, "error": "Unknown collection type"}, status=400)

    exclude_fields = ["id", "created_at"]
    fields = [
        field.name
        for field in model._meta.get_fields()
        if field.concrete
        and not field.many_to_many
        and field.name not in exclude_fields
    ]
    items = list(model.objects.values(*fields, "id"))
    html = render_to_string(
            "cms/collection_table.html", {"items": items, "fields": fields}
        )
    return JsonResponse({'html': html})
