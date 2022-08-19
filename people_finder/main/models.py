from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class ListofInterests(models.Model):
    interest = models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return self.interest

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    display_picture = models.ImageField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    

class Interest(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    interest1 = models.ForeignKey(ListofInterests, on_delete=models.CASCADE, related_name='user_interest')
    link = models.CharField(max_length=100)
    bio = models.CharField(max_length=140)