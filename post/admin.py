from django.contrib import admin
from .models import Comment, Like, Post, PostTag, Profile, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(PostTag)
