from django.test import TestCase
from site_backend.categories.models import Category


class TestCategoryModel(TestCase):
    def test_category_model(self):
        self.assertEqual(Category.objects.count(), 0)
        name = "Еда"
        category = Category.objects.create(name=name)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(category.name, name)
