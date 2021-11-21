from django.db import models

# Create your models here.

class User(models.Model):
	name        = models.CharField(max_length=20)
	email       = models.CharField(max_length=100, unique=True)
	password    = models.CharField(max_length=200)
	phonenumber = models.CharField(max_length=20)
	information = models.CharField(max_length=200, null=True)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'users'
