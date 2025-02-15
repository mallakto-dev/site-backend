import uuid
from django.db import models

from app.helpers import slugify_name


class Category(models.Model):
    """Goods category model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255, verbose_name="название")

    slug = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Генерируется автоматически на основе имени",
    )

    def save(self, *args, **kwargs) -> None:
        """
        add slug for creating Good object
        and save it
        """

        if not self.slug:
            self.slug = slugify_name(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Good(models.Model):
    """Model representing good"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255, verbose_name="Название")

    slug = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Генерируется автоматически на основе имени",
    )

    img_url = models.CharField(
        max_length=255, verbose_name="Ссылка на фото", blank=True
    )

    img_caption = models.CharField(
        max_length=255,
        verbose_name="Подпись",
        help_text="Для фото",
        blank=True,
    )

    alternative_text = models.CharField(
        max_length=255,
        verbose_name="Альтернативный текст",
        help_text="Для фото (важно для SEO и доступности)",
        blank=True,
    )

    description = models.TextField(
        verbose_name="Описание", max_length=1000, blank=True
    )

    price = models.DecimalField(
        verbose_name="Цена", max_digits=6, decimal_places=2
    )

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

    availability = models.BooleanField(verbose_name="Наличие")

    objects = models.Manager()

    def save(self, *args, **kwargs) -> None:
        """
        add slug for creating Good object
        and save it
        """

        if not self.slug:
            self.slug = slugify_name(self.name)
        super(Good, self).save(*args, **kwargs)

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class CategoryGoodRelation(models.Model):
    """
    Class representing shop item and its category relations
    table row will be deleted with good deletion,
    category deletion bounded to good will raise protected error
    """

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
