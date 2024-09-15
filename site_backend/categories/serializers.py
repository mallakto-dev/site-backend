from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for goods categories"""

    class Meta:
        model = Category
        fields = "__all__"
