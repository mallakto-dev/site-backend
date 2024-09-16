from rest_framework import serializers

from .models import Good, Category


class GoodSerializer(serializers.ModelSerializer):
    """
    Serializer for goods categories
    Include link to photo source
    """

    photo_path = serializers.SlugRelatedField(
        read_only=True, slug_field="source"
    )

    category = serializers.StringRelatedField()

    class Meta:
        model = Good
        fields = [
            "id",
            "name",
            "price",
            "ingredients",
            "category",
            "nutrition_facts",
            "nutrition_facts",
            "weight",
            "availability",
            "photo_path",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category include category goods"""

    items = GoodSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "items"]
