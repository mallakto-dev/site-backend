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

    photo_path = serializers.SlugRelatedField(
        read_only=True, slug_field="source"
    )

    category = BaseCategorySerializer()

    class Meta:
        model = Good
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "ingredients",
            "category",
            "nutrition_facts",
            "shelf_life",
            "weight",
            "availability",
            "photo_path",
        ]


class CategorySerializer(BaseCategorySerializer):
    """Serializer for category include category goods"""

    items = GoodSerializer(many=True)

    class Meta(BaseCategorySerializer.Meta):
        fields = ["id", "name", "slug", "items"]
