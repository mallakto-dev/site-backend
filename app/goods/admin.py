from django.contrib import admin

from .models import Category, Good


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ["name", "availability"]
    list_editable = ["availability"]
