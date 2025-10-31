from rest_framework import serializers
from bagback.models import Bagpack


class BagpackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bagpack
        fields = "__all__"
