# Generated by Django 5.2.1 on 2025-06-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_usermodel_password_usermodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='username',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
