# Generated by Django 5.2.1 on 2025-06-09 04:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_items_publisherid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='profile_img',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='MU_id',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='dept',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='profileImg',
            field=models.ImageField(blank=True, null=True, upload_to='profileImg/'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.OneToOneField(blank=True, max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
