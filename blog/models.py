from django.db import models
from django.utils import timezone

# Create your models here.
"""
    The Post model contains various elements of a blog post.

    The elements contained in the Post model are title, description,
    body, and date. I use these fields to display their respective
    data on my website.

    Class Meta allows me to set an 'ordering' variable (in this case it's date)
    that way things get order from oldest to newest (this is done by setting a '-' before the
    date variable).
"""
class Post(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 75)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #pub_date = models.DateTimeField(name='published date')

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.title
    

    def __str__(self):
        return self.body[:50]
    