from factory.django import DjangoModelFactory
import factory

from app.goods.models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("pystr", max_chars=8)
