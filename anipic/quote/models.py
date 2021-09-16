from django.db import models
from django.urls import reverse


class Quote(models.Model):
    quote = models.CharField(max_length=1000)
    said_by = models.CharField(max_length=100)
    tag = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.quote} by {self.said_by}"


    def get_absolute_url(self):
        return f"/quote/{self.id}"