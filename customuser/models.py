from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Myuser(AbstractUser):
    display_name = models.CharField(max_length=50,default='testuser')