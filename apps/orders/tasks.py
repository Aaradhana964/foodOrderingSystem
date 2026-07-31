import time
from .models import Order


def update_order_status(order_id):

    status_flow = [
        ("Confirmed", 10),
        ("Preparing", 30),
        ("Delivery", 60),
        ("Delivered", 90),
    ]

    for status, seconds in status_flow:

        time.sleep(seconds)

        try:
            order = Order.objects.get(id=order_id)
            order.status = status
            order.save()

        except Order.DoesNotExist:
            break