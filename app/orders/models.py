import uuid

from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from app.goods.models import Good


User = get_user_model()


class Order(models.Model):
    """Model representing order"""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    name = models.CharField(max_length=50, verbose_name="Имя")

    phone = PhoneNumberField(region="RU", max_length=12)

    email = models.EmailField()

    address = models.CharField(
        max_length=250, blank=True, verbose_name="Адрес"
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    payment_type = models.CharField(
        choices={"card": "Перевод", "cash": "Наличные"},
        verbose_name="Способ оплаты",
        max_length=8,
    )

    order_type = models.CharField(
        choices={"delivery": "Доставка", "pickup": "Самовывоз"},
        verbose_name="Способ доставки",
        max_length=9,
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Заказ {}".format(self.pk)

    @property
    def amount(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Model representing order items"""

    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Good, related_name="order_items", on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField(verbose_name="Количество")

    price = models.IntegerField(default=0)

    def save(self, *args, **kwargs) -> None:
        """
        Add contemporary good's price
        """
        price = self.product.price
        self.price = price

        super(OrderItem, self).save(*args, **kwargs)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self) -> str:
        return "{}".format(self.product.name)
