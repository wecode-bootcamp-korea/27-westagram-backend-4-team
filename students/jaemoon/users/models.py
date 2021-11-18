from django.db import models

# Create your models here.
class User(models.Modle):

    name     = models.CharField(max_length=20)
    email    = models.CharField(max_lenght=45)
    password = models.IntegerField(max_lenght=45)
    call_num = models.IntegerField(max_lenght=45)
    address = models.CharField(max_lenght=50)

    class Meta:
        db_table='users'