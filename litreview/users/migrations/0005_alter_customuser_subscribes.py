# Generated by Django 4.0.3 on 2022-03-31 22:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='subscribes',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]