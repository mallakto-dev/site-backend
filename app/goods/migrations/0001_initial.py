# Generated by Django 5.1.1 on 2024-10-09 17:18

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="название"),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Генерируется автоматически на основе имени",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Good",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название"),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Генерируется автоматически на основе имени",
                        max_length=255,
                    ),
                ),
                (
                    "img_url",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name="Ссылка на фото",
                    ),
                ),
                (
                    "img_caption",
                    models.CharField(
                        blank=True,
                        help_text="Для фото",
                        max_length=255,
                        verbose_name="Подпись",
                    ),
                ),
                (
                    "alternative_text",
                    models.CharField(
                        blank=True,
                        help_text="Для фото (важно для SEO и доступности)",
                        max_length=255,
                        verbose_name="Альтернативный текст",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=1000, verbose_name="Описание"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="Цена"
                    ),
                ),
                (
                    "ingredients",
                    models.TextField(max_length=1000, verbose_name="Состав"),
                ),
                (
                    "nutrition_facts",
                    models.CharField(
                        max_length=255, verbose_name="Пищевая ценность"
                    ),
                ),
                (
                    "shelf_life",
                    models.CharField(
                        max_length=100, verbose_name="Срок годности"
                    ),
                ),
                ("weight", models.IntegerField(verbose_name="Вес")),
                ("availability", models.BooleanField(verbose_name="Наличие")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="items",
                        to="goods.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.CreateModel(
            name="CategoryGoodRelation",
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="goods.category",
                    ),
                ),
                (
                    "good",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="goods.good",
                    ),
                ),
            ],
        ),
    ]
