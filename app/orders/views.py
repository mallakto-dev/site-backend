import os

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Order
from .serializers import OrderCreateSerializer
from app.orders.mailer import OrderConfirmationMessage


class OrderViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Order.objects
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create Order object, send confirmation message,
        return http response
        """

        response = super().create(request, *args, **kwargs)
        order = Order.objects.get(id=response.data["id"])
        self.send_email_confirmation(order)
        return response

    @staticmethod
    def send_email_confirmation(order) -> None:
        """
        Create confirmation message from Order object
        """

        subject = f"Подтверждение заказа №{order.id}. Mallakto"
        from_email = "malakto.dev@yandex.ru"
        to = [os.getenv("ADMIN_EMAIL"), order.email]
        msg = OrderConfirmationMessage(
            subject=subject, from_email=from_email, to=to
        )
        msg.render_body(order)
        msg.content_subtype = "html"
        msg.send()
