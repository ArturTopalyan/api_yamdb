from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название жанра',
    )
    slug = models.SlugField(
        unique=True,
        max_length=20,
        verbose_name='Часть URL адреса группы',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
