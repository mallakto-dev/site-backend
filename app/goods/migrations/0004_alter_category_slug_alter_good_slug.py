# Generated by Django 5.1.1 on 2024-10-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0003_category_slug_good_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="good",
            name="slug",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
