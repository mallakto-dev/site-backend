from factory.django import DjangoModelFactory
from app.goods.models import Good


class GoodFactory(DjangoModelFactory):
    class Meta:
        model = Good

    name = "Товар"

    price = "200"

    ingredients = "Вода, соя, соль, хлористый магний"

    nutrition_facts = " 73 кКал/304 кДж Белки 8,7г, Жиры 3,7г, Углеводы 1,7г"

    shelf_life = "21 день"

    weight = 400

    availability = True
