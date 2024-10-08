from django.db.models.signals import post_save
from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]


class OrderCreateSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(
        required=True, many=True, source="items", allow_null=False
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "username",
            "name",
            "phone",
            "email",
            "address",
            "payment_type",
            "order_type",
            "order_items",
        ]

    def to_internal_value(self, data):
        """
        Check if order items field contains any item,
        to prevent creation of order not containing any items
        """

        if not data["order_items"]:
            data["order_items"] = None
        return super(OrderCreateSerializer, self).to_internal_value(data)

    def create(self, validated_data) -> Order:
        """
        Create OrderItem objects from order_items field
        and send a signal after all order items created
        """

        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        post_save.send(sender=self.__class__, order=order)
        return order
