# Generated by Django 3.2.9 on 2021-11-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='call_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.IntegerField(),
        ),
    ]
