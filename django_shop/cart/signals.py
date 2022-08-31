from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart


@receiver(post_save, sender='account.User')
def create_cart(instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
