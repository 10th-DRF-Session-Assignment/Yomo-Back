from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'com_writer', 'com_comment', 'create_time', 'post_id']


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'hook_text', 'writer',
                  'content', 'created_time', 'comment']
