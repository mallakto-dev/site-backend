from rest_framework import serializers

from .models import Good, Category


class BaseCategorySerializer(serializers.ModelSerializer):
    """
    Base category serializer items not included
    """

    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class GoodSerializer(serializers.ModelSerializer):
    """
    Serializer for goods categories
    Include link to photo source
    """

    category = BaseCategorySerializer()

    class Meta:
        model = Good
        fields = [
            "id",
            "name",
            "slug",
            "photo_path",
            "price",
            "ingredients",
            "category",
            "nutrition_facts",
            "shelf_life",
            "weight",
            "availability",
        ]


class CategorySerializer(BaseCategorySerializer):
    """Serializer for category include category goods"""

    items = GoodSerializer(many=True)

    class Meta(BaseCategorySerializer.Meta):
        fields = ["id", "name", "slug", "items"]
