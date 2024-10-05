from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from app.goods.tests.factories.category_factory import CategoryFactory
from app.goods.tests.factories.good_factory import GoodFactory
from app.orders.models import Order


client = APIClient()


class TestOrderPost(TestCase):

    def test_order_post_valid(self):
        self.assertEqual(Order.objects.count(), 0)

        order_item = GoodFactory(category=CategoryFactory())

        order_data = {
            "name": "test",
            "phone": "+79999999999",
            "email": "test@test.com",
            "address": "test address",
            "payment_type": "card",
            "order_type": "delivery",
            "order_items": [{"product": order_item.id, "quantity": 2}],
        }

        response = client.post(
            reverse("order-list"), order_data, format="json"
        )

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(Order.objects.count(), 1)

        database_order = Order.objects.last()
        self.assertEqual(order_data["email"], database_order.email)
        self.assertEqual(order_data["phone"], database_order.phone)
        self.assertEqual(order_data["name"], database_order.name)
        self.assertEqual(order_data["address"], database_order.address)
        self.assertEqual(
            order_data["payment_type"], database_order.payment_type
        )
        self.assertEqual(order_data["order_type"], database_order.order_type)
        self.assertEqual(
            order_data["order_items"][0]["product"],
            database_order.items.all()[0].product.id,
        )
        self.assertEqual(
            order_data["order_items"][0]["quantity"],
            database_order.items.all()[0].quantity,
        )

    def test_post_missing_name(self):
        self.assertEqual(Order.objects.count(), 0)

        order_item = GoodFactory(category=CategoryFactory())

        order_data = {
            "phone": "+79999999999",
            "email": "test@test.com",
            "address": "test address",
            "payment_type": "card",
            "order_type": "delivery",
            "order_items": [{"product": order_item.id, "quantity": 2}],
        }

        response = client.post(
            reverse("order-list"), order_data, format="json"
        )

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.content, b'{"name":["This field is required."]}'
        )
        self.assertEqual(Order.objects.count(), 0)

    def test_post_missing_phone(self):
        self.assertEqual(Order.objects.count(), 0)

        order_item = GoodFactory(category=CategoryFactory())

        order_data = {
            "name": "test",
            "email": "test@test.com",
            "address": "test address",
            "payment_type": "card",
            "order_type": "delivery",
            "order_items": [{"product": order_item.id, "quantity": 2}],
        }

        response = client.post(
            reverse("order-list"), order_data, format="json"
        )

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.content, b'{"phone":["This field is required."]}'
        )
        self.assertEqual(Order.objects.count(), 0)

    def test_post_missing_email(self):
        self.assertEqual(Order.objects.count(), 0)

        order_item = GoodFactory(category=CategoryFactory())

        order_data = {
            "name": "test",
            "phone": "+79999999999",
            "address": "test address",
            "payment_type": "card",
            "order_type": "delivery",
            "order_items": [{"product": order_item.id, "quantity": 2}],
        }

        response = client.post(
            reverse("order-list"), order_data, format="json"
        )

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.content, b'{"email":["This field is required."]}'
        )
        self.assertEqual(Order.objects.count(), 0)
