from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from bagback.models import Bagpack
from .serializers import BagpackSerializer


class BagpackViewSet(viewsets.ModelViewSet):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["season"]
    search_fields = ["name", "season"]
    permission_classes_by_action = {
        "list": [],
        "retrieve": [],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_permissions(self):
        return [
            permission()
            for permission in self.permission_classes_by_action.get(self.action, [])
        ]
