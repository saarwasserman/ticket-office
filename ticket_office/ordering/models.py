from django.db import models


class Order(models.Model):

    user = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    order_total = models.IntegerField()
    order_placed = models.DateTimeField(auto_now_add=True)
    order_paid = models.BooleanField(default=False)


class OrderLine(models.Model):

    ticket_amount = models.IntegerField()
    event = models.ForeignKey('event_catalog.Event', related_name='order_lines', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
