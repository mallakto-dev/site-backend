# Generated by Django 5.1.1 on 2024-09-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
