from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, post_tweet

urlpatterns = [
    path('', home, name='home'),
    path('post_tweet', post_tweet, name='post_tweet'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)