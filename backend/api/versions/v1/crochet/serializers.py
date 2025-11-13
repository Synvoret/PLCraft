from rest_framework import serializers
from apps.crochet.models import Crochet


class CrochetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crochet
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters long."
            )
        return value
