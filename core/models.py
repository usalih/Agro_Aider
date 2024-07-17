from django.db import models
from userauths.models import User
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
import uuid


# Create your models here.
# core/models.py
def user_file_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.id}/{filename}'

class Product(models.Model):
    name = models.CharField(max_length=255, default='')  # Default to an empty string
    description = models.TextField(default='')  # Default to an empty string
    category = models.CharField(max_length=50, choices=[('article', 'Article'), ('video', 'Video'), ('file', 'File')], default='article')  # Default to 'article'
    article = models.TextField(null=True, blank=True, default='input your article')  # Default to an empty string
    video = models.URLField(null=True, blank=True, default='input the video url here')  # Default to an empty string
    file = models.FileField(upload_to=user_file_directory_path, null=True, blank=True, default='')  # Default to an empty string
    image = models.ImageField(upload_to='images/', default='')  # Default to an empty string

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=255, default='')
    email = models.EmailField( default='')
    phone_no = models.CharField(max_length=15,  default='')
    message = models.TextField( max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    # comment = models.OneToOneField('self', related_name='parent', on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return f'Comment by {self.user.username} on {self.product.name}'
        except :
            return f'Commment no author on {self.content}'
        