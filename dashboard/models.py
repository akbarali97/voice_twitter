from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.FileField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
