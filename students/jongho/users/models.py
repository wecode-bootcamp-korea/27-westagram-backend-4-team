from django.db import models
class User(models.Model):
    
    id         =models.AutoField(primary_key=True)
    name       =models.CharField(max_length=100)
    email      =models.EmailField(unique=True)
    password   =models.IntegerField(max_length=200)
    contact    =models.CharField(max_length=100)
    information=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
# Create your models here.
