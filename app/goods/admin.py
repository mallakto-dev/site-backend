from django.contrib import admin

from .models import Category, Good


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ["name", "availability"]
    list_editable = ["availability"]
    fields = [
        "name",
        "img_url",
        "img_caption",
        "alternative_text",
        "description",
        "price",
        "ingredients",
        "category",
        "nutrition_facts",
        "shelf_life",
        "weight",
        "availability",
    ]
