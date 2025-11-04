from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from crochet.models import Crochet
from .serializers import CrochetSerializer


class CrochetListView(generics.ListAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer


class CrochetCreateView(generics.CreateAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    parser_classes = (MultiPartParser, FormParser)


class CrochetDetailView(generics.RetrieveAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"


class CrochetUpdateView(generics.UpdateAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)


class CrochetDeleteView(generics.DestroyAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"
