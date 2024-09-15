from django.db import models


class Category(models.Model):
    """Goods category model"""

    name = models.CharField(max_length=255, verbose_name="название")

    def __str__(self) -> models.CharField:
        return self.name
