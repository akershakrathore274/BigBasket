from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    mobile=models.CharField(max_length=10,blank=True)