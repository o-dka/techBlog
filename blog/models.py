from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True
        )

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True,
        null=True
        )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
