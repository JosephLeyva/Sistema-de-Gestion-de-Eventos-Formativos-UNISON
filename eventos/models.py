from django.db import models
from django.contrib.auth.models import User,Group, AbstractUser
from django.db.models.base import Model

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100,null=True)