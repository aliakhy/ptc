from django.db.models.signals import pre_save
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete
from .models import Project, Gallery


@receiver(pre_save, sender=Gallery)
def del_old_image(sender, instance, **kwargs):

    if not instance.pk:
        return
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return
    old_image = getattr(old_instance, "image")
    new_image = getattr(instance, "image")
    if old_image and old_image.name != new_image.name:
        try:
            os.remove(old_image.path)
        except Exception:
            pass


@receiver(post_delete, sender=Gallery)
def delete_image_on_delete(sender, instance, **kwargs):

    image = getattr(instance, "image")
    if image:
        try:
            os.remove(image.path)
        except:
            pass
