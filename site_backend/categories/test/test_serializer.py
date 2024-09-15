from django.test import TestCase

from site_backend.categories.models import Category
from site_backend.categories.serializers import CategorySerializer


class TestCategorySerializer(TestCase):

    def test_category_Serializer(self):
        category = Category(name="Имя")
        serialized_category = CategorySerializer(category)
        self.assertEqual(serialized_category.data["name"], category.name)
        self.assertEqual(serialized_category.data["id"], category.pk)
