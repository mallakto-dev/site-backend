import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from app.orders.mailer import OrderConfirmationMessage
from app.orders.models import Order


@receiver(post_save, sender=Order)
def send_email_confirmation(instance, **kwargs):
    """
    Send confirmation email to admin and customer
    when order created or changed
    """

    order = instance

    subject = f"Подтверждение заказа №{order.id}. Mallakto"
    from_email = "malakto.dev@yandex.ru"
    to = [os.getenv("ADMIN_EMAIL"), order.email]

    msg = OrderConfirmationMessage(
        subject=subject, from_email=from_email, to=to
    )
    msg.render_body(order)
    msg.send()
