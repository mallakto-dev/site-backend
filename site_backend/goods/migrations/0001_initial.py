# Generated by Django 5.1.1 on 2024-09-15 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Good",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Название"),
                ),
                ("price", models.IntegerField(verbose_name="Цена")),
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
                        max_length=50, verbose_name="Срок годности"
                    ),
                ),
                ("weight", models.IntegerField(verbose_name="Вес")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="category",
                        to="categories.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
        ),
    ]
