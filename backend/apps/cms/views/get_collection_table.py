from django.http import JsonResponse
from django.template.loader import render_to_string

from apps.bagpack.models import Bagpack
from apps.crochet.models import Crochet


def get_collection_table(request):
    collection_type = request.GET.get("collection_type")
    if collection_type == "bagpack":
        items = Bagpack.objects.all()
        html = render_to_string("cms/collection_table.html", {"items": items})
    elif collection_type == "crochet":
        items = Crochet.objects.all()
        html = render_to_string("cms/collection_table.html", {"items": items})
    else:
        html = "<p>Unknown collection type.</p>"
    return JsonResponse({"html": html})
