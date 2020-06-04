from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #pub_date = models.DateTimeField(name='published date')

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.title
    

    def __str__(self):
        return self.body[:50]
    