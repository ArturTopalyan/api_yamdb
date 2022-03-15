from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """биографию, дату рождения, должность, фотографию или что-нибудь ещё"""
    
    biography = models.TextField()
    birth_day = models.DateField()
    photo = models.BinaryField()
    job_title = models.CharField(max_length=100)
