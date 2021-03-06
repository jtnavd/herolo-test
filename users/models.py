from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Update image size
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# OLD MODEL
# class Message(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     date_sent = models.DateTimeField(default = timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("message-detail", kwargs={"pk": self.pk})
    

class Mail(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_sent = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("message-detail", kwargs={"pk": self.pk})

