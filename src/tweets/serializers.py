from rest_framework import serializers
from .models import Post, Likes, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_identifier', 'title', 'topic', 'publish_time', 'message_body', 'expiration_time', 'author', 'status')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'author', 'post', 'created_on')

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ('like_or_dislike', 'author', 'post', 'created_on')