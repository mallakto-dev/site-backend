import django.db.models.deletion
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
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="название"),
                ),
            ],
        ),
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
                    "availability",
                    models.CharField(
                        choices=[
                            ("YES", "В наличии"),
                            ("NO", "Нет в наличии"),
                        ],
                        default="NO",
                        max_length=20,
                        verbose_name="Наличие",
                    ),
                ),
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
        migrations.CreateModel(
            name="GoodPhoto",
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
                ("source", models.CharField(max_length=255)),
                (
                    "good",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="good",
                        to="goods.good",
                        verbose_name="Товар",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GoodPhotoRelation",
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
                    "good",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="goods.good",
                    ),
                ),
                (
                    "photo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="goods.goodphoto",
                    ),
                ),
            ],
        ),
    ]
