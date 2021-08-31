from django.contrib.auth.models import User
from .models import WallPaper
from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete, sender=User)
def post_delete_cleanup(sender, instance, **kwargs):
    pass