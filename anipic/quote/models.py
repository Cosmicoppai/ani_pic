from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=1000, unique=True)
    tag = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.quote}   -   {self.tag}"


    def get_absolute_url(self):
        return f"/quote/{self.id}"