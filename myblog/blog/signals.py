# blog/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Category

@receiver(pre_save, sender=Category)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:  # Если slug пустой
        instance.slug = slugify(instance.name) or "default-slug"