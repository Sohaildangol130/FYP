from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures")
    facebook_link = models.TextField(blank=True)
    instagram_link = models.TextField(blank=True)
    behance_link = models.TextField(blank=True)
    linkedin_link = models.TextField(blank=True)