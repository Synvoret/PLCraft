from rest_framework import generics
from bagback.models import Bagpack
from .serializers import BagpackSerializer


class BagpackView(generics.ListCreateAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer


class BackpackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"
