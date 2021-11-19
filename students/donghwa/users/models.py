from django.db import models

# Create your models here.

class User(models.Model):
    name        = models.CharField(max_length=10)
    email       = models.CharField(max_length=45)
    password    = models.CharField(max_length=30)
    contacts    = models.IntegerField(max_length=11)
    address     = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_tables = 'users'


