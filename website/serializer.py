from rest_framework import serializers
from .models import Blog, Comment, Like


class BlogSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'createdAt', 'updatedAt', 'like_count']
        read_only_fields = ['author', 'createdAt', 'updatedAt']

    def get_like_count(self, obj):
        return Like.objects.filter(blog=obj).count()

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
