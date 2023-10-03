from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    national_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username

