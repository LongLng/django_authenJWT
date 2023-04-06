from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager


class User(AbstractBaseUser):
    username = None
    last_login = None
    is_staff = None
    is_superuser = None
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    objects     =   UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
	
 
    def __str__(self):
        return self.email

