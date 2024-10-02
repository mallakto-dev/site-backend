from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .factories.category_factory import CategoryFactory
from .factories.good_factory import GoodFactory


class TestGoodViewSet(TestCase):

    def test_good_list_access(self):
        response = self.client.get(reverse("good-list"))

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_good_list_content(self):
        item1 = GoodFactory(category=CategoryFactory())
        item2 = GoodFactory(category=CategoryFactory())

        response = self.client.get(reverse("good-list"))
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            item1.category.name, response.data[0]["category"]["name"]
        )
        self.assertEqual(
            item2.category.name, response.data[1]["category"]["name"]
        )
        self.assertEqual(item1.name, response.data[0]["name"])
        self.assertEqual(item2.name, response.data[1]["name"])

    def test_good_detail_view(self):
        item = GoodFactory(category=CategoryFactory())

        response = self.client.get(
            reverse("good-detail", kwargs={"pk": item.pk})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(item.id, response.data.get("id"))
        self.assertEqual(item.name, response.data.get("name"))
