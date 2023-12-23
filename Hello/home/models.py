from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
    

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])])

    def __str__(self):
        return self.title

class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

class Dislike(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)