from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=10)
    email       = models.EmailField(max_length=45, unique = True)
    password    = models.CharField(max_length=200)
    contacts    = models.IntegerField(max_length=20)
    address     = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
