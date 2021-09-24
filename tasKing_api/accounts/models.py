from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=128)
    email = models.EmailField(('email address'),unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=256)
    company = models.CharField(max_length=256,blank=True,null=True)



