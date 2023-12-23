# Generated by Django 5.0 on 2023-12-22 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_video_like_dislike_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='duration',
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])]),
        ),
    ]