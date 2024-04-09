# Generated by Django 5.0.3 on 2024-04-03 10:10

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_cart_user_remove_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='article',
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(default='default_video.mp4', upload_to=core.models.user_file_directory_path),
        ),
    ]
