from django.db import models

# Create your models here.

class User(models.Model):
    Name        = models.CharField(max_length=10)
    Email       = models.CharField(max_length=45)
    Password    = models.CharField(max_length=30)
    Contacts    = models.IntegerField(max_length=11)
    Address     = models.CharField(max_length=100)

    class Meta:
        db_tables = 'users'
