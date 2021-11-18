from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(max_length=20)
    email       = models.CharField(max_lenght=45,unique=True)
    password    = models.IntegerField(max_lenght=200)
    call_num    = models.IntegerField(max_lenght=45)
    address     = models.CharField(max_lenght=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='users'