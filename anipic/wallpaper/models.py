from django.db import models


class WallPaper(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='')
    tag = models.CharField(max_length=8)
    is_nsfw = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.title} - {self.image} - {self.created}"

    def get_absolute_url(self):
        return reverse('pics', kwargs={'tag': self.tag})