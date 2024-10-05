from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestOrderViewAccess(TestCase):

    def test_access(self):
        response = self.client.get(reverse("order-list"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
