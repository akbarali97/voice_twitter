from django.urls import path
from .views import login, home

urlpatterns = [
    path('', home, name='sso_home'),
    path('login', login, name='sso_login'),
]