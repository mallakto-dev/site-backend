import uuid
from django.db import models

from app.helpers import slugify_name


class Category(models.Model):
    """Goods category model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255, verbose_name="название")

    slug = models.CharField(max_length=255, blank=True, default="")

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify_name(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> models.CharField:
        return self.name


class Good(models.Model):
    """Model representing good"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255, verbose_name="Название")

    slug = models.CharField(max_length=255, blank=True, default="")

    price = models.IntegerField(verbose_name="Цена")

    ingredients = models.TextField(verbose_name="Состав", max_length=1000)

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.PROTECT,
        related_name="items",
    )

    nutrition_facts = models.CharField(
        max_length=255, verbose_name="Пищевая ценность"
    )

    shelf_life = models.CharField(max_length=100, verbose_name="Срок годности")

    weight = models.IntegerField(verbose_name="Вес")

    availability = models.BooleanField()

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify_name(self.name)
        super(Good, self).save(*args, **kwargs)

    def __str__(self) -> models.CharField:
        return self.name

    def get_price(self):
        return self.price


class GoodPhoto(models.Model):
    """
    Class representing shop item photo source
    """

    good = models.ForeignKey(
        to=Good,
        on_delete=models.CASCADE,
        verbose_name="Товар",
        related_name="good",
    )

    source = models.CharField(max_length=255)


class GoodPhotoRelation(models.Model):
    """
    Class representing shop item and its photo relations
    table row will be deleted with good deletion
    """

    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    photo = models.ForeignKey(GoodPhoto, on_delete=models.SET_NULL, null=True)


class CategoryGoodRelation(models.Model):
    """
    Class representing shop item and its category relations
    table row will be deleted with good deletion,
    category deletion bounded to good will raise protected error
    """

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
