from django.db import models

class User(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100)
    email       = models.EmailField(unique=True)
    password    = models.CharField(max_length=200)
    phone       = models.CharField(max_length=200)
    information = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta():
      db_table="users"
    
    def __str__(self):
      return self.name

# Create your models here.