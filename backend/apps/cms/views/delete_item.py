from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from apps.bagpack.models import Bagpack
from apps.crochet.models import Crochet


@require_POST
def delete_item(request):
    collection_type = request.POST.get("collection_type")
    pk = request.POST.get("id")
    print(collection_type)

    if not collection_type or not pk:
        return HttpResponseBadRequest("Missing parameters.")

    if collection_type == "bagpack":
        model = Bagpack
    elif collection_type == "crochet":
        model = Crochet
    else:
        return JsonResponse({"html": "<p>Unknown collection type.</p>"})

    obj = get_object_or_404(model, pk=pk)
    obj.delete()

    exclude_fields = ["id", "created_at"]
    fields = [
        field.name
        for field in model._meta.get_fields()
        if field.concrete
        and not field.many_to_many
        and field.name not in exclude_fields
    ]
    items = model.objects.values(*fields, "id")

    html = render_to_string(
        "cms/collection_table.html",
        {"items": items, "fields": fields, "collection_type": collection_type},
    )

    return JsonResponse({"ok": True, "html": html})
