from rest_framework import serializers
from .models import Channel


class ChannelNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "id",
            "name",
            "city",
            "voivodeship",
            "flat_no",
            "street",
            "postal_code",
            "house_no",
            "email",
            "epuap",
        ]
