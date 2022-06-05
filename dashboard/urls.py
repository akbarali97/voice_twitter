from django.urls import path
from .views import home, post_tweet

urlpatterns = [
    path('', home, name='home'),
    path('post_tweet', post_tweet, name='post_tweet_ajax'),
]