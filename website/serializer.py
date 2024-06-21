from rest_framework import serializers
from .models import Blog, Comment, Like


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'createdAt', 'updatedAt']
        read_only_fields = ['author', 'createdAt', 'updatedAt']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'blog']
        read_only_fields = ['user']
