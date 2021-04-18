from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Post', views.PostViewSet)
router.register(r'Likes', views.LikesViewSet)
router.register(r'Comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]