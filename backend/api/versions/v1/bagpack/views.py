from rest_framework import generics
from bagback.models import Bagpack
from .serializers import BagpackSerializer


class BagpackListView(generics.ListAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer


class BagpackCreateView(generics.CreateAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer


class BagpackDetailView(generics.RetrieveAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"


class BagpackUpdateView(generics.UpdateAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"


class BagpackDeleteView(generics.DestroyAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"
