# Generated by Django 5.1.1 on 2025-02-15 15:01

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("goods", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=16, region="RU"
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=250, verbose_name="Адрес"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Создан"
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("card", "Перевод"), ("cash", "Наличные")],
                        max_length=8,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "order_type",
                    models.CharField(
                        choices=[
                            ("delivery", "Доставка"),
                            ("pickup", "Самовывоз"),
                        ],
                        max_length=9,
                        verbose_name="Способ доставки",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(verbose_name="Количество"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0"),
                        max_digits=7,
                        verbose_name="Цена",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_items",
                        to="goods.good",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент заказа",
                "verbose_name_plural": "Элементы заказа",
            },
        ),
    ]
