from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('Correo', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
