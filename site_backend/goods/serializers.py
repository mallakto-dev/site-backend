from rest_framework import serializers

from .models import Good


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for goods categories"""

    class Meta:
        model = Good
        fields = "__all__"
