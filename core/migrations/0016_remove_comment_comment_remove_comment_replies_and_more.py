# Generated by Django 5.0.3 on 2024-07-10 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='replies',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
