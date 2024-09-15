from django.db import models

from site_backend.categories.models import Category


class Good(models.Model):
    """Model representing good"""

    name = models.CharField(max_length=255, verbose_name="Название")

    price = models.IntegerField(verbose_name="Цена")

    ingredients = models.TextField(verbose_name="Состав", max_length=1000)

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.PROTECT,
        related_name="category",
    )

    nutrition_facts = models.CharField(
        max_length=255, verbose_name="Пищевая ценность"
    )

    shelf_life = models.CharField(max_length=50, verbose_name="Срок годности")

    weight = models.IntegerField(verbose_name="Вес")
