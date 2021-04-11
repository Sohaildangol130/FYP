from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class all_posts(models.Model):
    post_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="all_posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)