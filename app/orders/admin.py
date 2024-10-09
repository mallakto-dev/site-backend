from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    field = ["product", "quantity"]
    exclude = ["price"]
    readonly_fields = ["cost"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    readonly_fields = ["username", "amount"]
