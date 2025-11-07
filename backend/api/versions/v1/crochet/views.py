from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from crochet.models import Crochet
from .serializers import CrochetSerializer


class CrochetListCreateView(generics.ListCreateAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["name", "category"]
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return []


class CrochetDetailView(generics.RetrieveAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"


class CrochetUpdateView(generics.UpdateAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminUser]


class CrochetDeleteView(generics.DestroyAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"
    permission_classes = [IsAdminUser]
