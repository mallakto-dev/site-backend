from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .factories.category_factory import CategoryFactory


class TestCategoryViewSet(TestCase):

    def test_category_list_access(self):
        response = self.client.get(reverse("category-list"))

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_category_list_content(self):
        category1 = CategoryFactory()
        category2 = CategoryFactory()

        response = self.client.get(reverse("category-list"))
        self.assertIn(bytes(category1.name, "utf-8"), response.content)
        self.assertIn(bytes(category2.name, "utf-8"), response.content)
        self.assertEqual(len(response.data), 2)

    def test_category_detail_view(self):
        category = CategoryFactory()

        response = self.client.get(
            reverse("category-detail", kwargs={"pk": category.pk})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(bytes(category.name, "utf-8"), response.content)
        self.assertIsInstance(response.data, dict)
