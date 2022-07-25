from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    hook_text = models.CharField(max_length=200)
    content = models.TextField()


class Comment(models.Model):
    com_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    com_comment = models.TextField(max_length=8000)
    create_time = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment')
