from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Likes, Comment
from .serializers import PostSerializer, LikesSerializer, CommentSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

    def get__post_queryset(self):
        "Return attributes of particular post"
        queryset = Post.objects.all()
        post_title = self.request.query_params.GET.get('title', None)
        if post_title is not None:
            queryset = queryset.filter(title=post_topic)
        return queryset

    def get_topic_queryset(self):
        "Return posts of particular topic"
        post_topic = self.request.query_params.get('topic')

        if post_topic is not None:
            queryset = Post.objects.all().filter(~Q(topic = 'tech'))
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('comment')
    serializer_class = CommentSerializer

    def get_queryset(self):
        "Return attributes of particular post"
        queryset = Comment.objects.all()
        post = self.request.query_params.get('post')

        if post is not None:
            queryset = queryset.filter(post = post)
        return queryset

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all().order_by('first_name')
    serializer_class = LikesSerializer
    
    def get_queryset(self):
        "Return attributes of particular post"
        queryset = Likes.objects.all()
        post = self.request.query_params.get('post')

        if post is not None:
            queryset = queryset.filter(post = post)
        return queryset