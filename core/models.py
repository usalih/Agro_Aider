from django.db import models
from userauths.models import User
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField


# Create your models here.
# core/models.py
def user_file_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.id}/{filename}'

class Product(models.Model):
    name = models.CharField(max_length=255, default='')  # Default to an empty string
    description = models.TextField(default='')  # Default to an empty string
    category = models.CharField(max_length=50, choices=[('article', 'Article'), ('video', 'Video'), ('file', 'File')], default='article')  # Default to 'article'
    article = models.TextField(null=True, blank=True, default='')  # Default to an empty string
    video = models.URLField(null=True, blank=True, default='')  # Default to an empty string
    file = models.FileField(upload_to=user_file_directory_path, null=True, blank=True, default='')  # Default to an empty string
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='')  # Default to an empty string

    def __str__(self):
        return self.name

