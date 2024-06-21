from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]


class Like(models.Model):
    blog = models.ForeignKey(Blog, related_name='like', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'blog')

    def __str__(self):
        return f'{self.user} likes {self.blog.title}'