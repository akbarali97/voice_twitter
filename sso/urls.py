from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='sso_home'),
    path('accounts/', include('allauth.urls')),
]