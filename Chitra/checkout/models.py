from django.db import models
from posts.models import all_posts
from django.contrib.auth.models import User

# Create your models here.
class checkout(models.Model):
    product = models.ForeignKey(all_posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    zone = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()