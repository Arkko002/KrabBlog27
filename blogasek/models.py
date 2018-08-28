from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    text = models.CharField(max_length=8000)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return "{0} - {1}".format(self.author.nick, self.pub_date)
