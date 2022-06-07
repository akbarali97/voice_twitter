from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, post_tweet, post_comment

urlpatterns = [
    path('', home, name='home'),
    path('post_tweet', post_tweet, name='post_tweet'),
    path('post_comment', post_comment, name='post_comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)