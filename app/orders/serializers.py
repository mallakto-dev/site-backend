from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["product"]


class OrderCreateSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(many=True, source="items")

    class Meta:
        model = Order
        fields = [
            "username",
            "name",
            "phone",
            "email",
            "address",
            "payment_type",
            "order_type",
            "order_items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
