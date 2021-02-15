from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from ..event_catalog.models import Event


class Basket(models.Model):

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)


class BasketLine(models.Model):

    ticket_amount = models.IntegerField()
    event = models.OneToOneField('event_catalog.Event', related_name='basket_lines', on_delete=models.CASCADE)
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_basket(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_basket(sender, instance, **kwargs):
    instance.basket.save()
