from django.core.mail import EmailMultiAlternatives


class OrderConfirmationMessage(EmailMultiAlternatives):

    def render_body(self, order):
        order_items = order.items.all()
        order_table = ""
        for item in order_items:
            order_table += f"""<tr style="border: 1px solid black;">
<td style="border: 1px solid black;padding: 10px;">{item.product.name}</td>
<td style="border: 1px solid black;padding: 10px;">{item.quantity}</td>
<td style="border: 1px solid black;padding: 10px;">{item.price}</td>
</tr>"""

        message = f"""<h1>Заказ №{order.id}</h1>
        <table style="border: 1px solid black;
              border-collapse: collapse;text-align: center;">
                <tr style="border: 1px solid black;">
<th style="border: 1px solid black; padding: 10px;font-size:18px;"> \
Наименование</th>
    <th style="border: 1px solid black; padding: 10px;font-size:18px;"> \
    Кол-во</th>
    <th style="border: 1px solid black; padding: 10px;font-size:18px;"> \
    Цена</th>
                </tr>
                {order_table}
              </table>
              <p><strong>Всего:</strong> {order.amount}</p>
              <h2>Контактные данные</h2>
              <p><strong>Имя:</strong> {order.name}</p>
              <p><strong>Телефон:</strong> {order.phone}</p>
<p><strong>Способ доставки:</strong> {order.get_order_type_display()}</p>
              <p><strong>Адрес:</strong> {order.address}</p>
<p><strong>Тип оплаты:</strong> {order.get_payment_type_display()}</p>"""

        self.body = message
        self.content_subtype = "html"
