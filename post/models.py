from django.db import models

class Post(models.Model):

    title = models.CharField(max_length = 200)
    author = models.CharField (max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        