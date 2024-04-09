# Generated by Django 5.0.3 on 2024-04-03 11:02

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_description_product_article_product_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(default='input attached file docs and videos', upload_to=core.models.user_file_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Latest Update.', max_length=100),
        ),
    ]
