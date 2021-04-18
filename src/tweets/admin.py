from django.contrib import admin
from .models import Post, Comment, Likes

# Register your models here.
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("num_comments", "comment", "author", "post", "created_on")
    list_filter = ("comment", "num_comments", "author", "post")
    search_fields = ("comment")
    actions = ["approve_comments"]


