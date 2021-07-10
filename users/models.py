from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Mail(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField
    crea

