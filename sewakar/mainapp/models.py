from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userext(models.Model):
    specification = models.CharField(max_length= 15)
    user = models.OneToOneField(User,on_delete=models.CASCADE)