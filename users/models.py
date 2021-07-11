from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Profile(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_sent = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

