from rest_framework import generics
from crochet.models import Crochet
from .serializers import CrochetSerializer


class CrochetView(generics.ListCreateAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer


class CrochetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer
    lookup_field = "pk"
