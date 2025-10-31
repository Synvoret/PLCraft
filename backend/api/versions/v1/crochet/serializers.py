from rest_framework import serializers
from crochet.models import Crochet


class CrochetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crochet
        fields = "__all__"
