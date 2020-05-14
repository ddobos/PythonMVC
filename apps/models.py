from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_at = models.DataTimeFiled(auto_now_add=True)
    update_at = models.DataTimeFiled(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.author.first_name}'

