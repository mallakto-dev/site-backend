from django.test import TestCase

from site_backend.goods.models import Good
from .factory.good_factory import GoodFactory
from site_backend.categories.models import Category


class TestGoodModel(TestCase):
    def test_good_model(self):
        self.assertEqual(Good.objects.count(), 0)
        good = GoodFactory(category_id=Category.objects.create(name="Имя").id)
        self.assertEqual(Good.objects.count(), 1)
        self.assertEqual(good.name, "Товар")
