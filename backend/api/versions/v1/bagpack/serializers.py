from rest_framework import serializers
from bagback.models import Bagpack


class BagpackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bagpack
        fields = "__all__"
        read_only_fields = ["id"]

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters long."
            )
        return value
