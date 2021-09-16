from .models import WallPaper
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=WallPaper)
def post_delete_cleanup(sender, instance, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)