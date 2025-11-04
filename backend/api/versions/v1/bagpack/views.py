from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from bagback.models import Bagpack
from .serializers import BagpackSerializer


class BagpackListView(generics.ListAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer


class BagpackCreateView(generics.CreateAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    parser_classes = (MultiPartParser, FormParser)


class BagpackDetailView(generics.RetrieveAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"


class BagpackUpdateView(generics.UpdateAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)


class BagpackDeleteView(generics.DestroyAPIView):
    queryset = Bagpack.objects.all()
    serializer_class = BagpackSerializer
    lookup_field = "pk"
