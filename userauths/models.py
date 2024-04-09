from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=100)
    username =models.CharField(max_length=100)
    
    # admin email login 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']




