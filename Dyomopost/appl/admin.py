from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email', 'school']
    list_display_links = ['id', 'username']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'hook_text', 'writer', 'created_time', 'comment']
    list_display_links = ['id', 'hook_text']
