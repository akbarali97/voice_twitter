from django.contrib import admin
from .models import Tweet, Comment

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass