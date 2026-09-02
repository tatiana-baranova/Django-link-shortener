from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Користувач'
    )

    original_url = models.URLField(
        max_length=250,
        verbose_name='Оригінальне посилання'
    )

    short_url = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Скорочене посилання'
    )

    def __str__(self):
        return self.short_url