from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    question = models.CharField(max_length=200)
    text = models.TextField()
    synopsis = models.TextField(default="null")
    slug = models.SlugField(max_length=120, unique=True, default="null")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question