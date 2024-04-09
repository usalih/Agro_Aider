from . import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=models.User)
def create_cart_model(sender, instance, created, *args, **kwargs):
    if created and not (instance.is_staff or instance.is_superuser):
        models.Cart.objects.get_or_create(user=instance, defaults={"user": instance})
