from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.apps import apps
from . models import Profile

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created and not Profile.objects.filter(user=instance).exists():
        profile = Profile(user=instance)
        # Set the default avatar here
        profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
