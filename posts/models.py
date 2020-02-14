from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    catagory = models.CharField(max_length=150)
    desc = models.CharField(max_length=500)
    body = models.TextField()
    live = models.BooleanField()

    @property
    def url(self):
        return f'/{self.catagory}/{self.pk}'