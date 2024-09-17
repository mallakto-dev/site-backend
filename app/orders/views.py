from rest_framework import viewsets, mixins

from .models import Order
from .serializers import OrderCreateSerializer


class OrderViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Order.objects
    serializer_class = OrderCreateSerializer
