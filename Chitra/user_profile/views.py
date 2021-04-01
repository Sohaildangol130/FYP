from django.shortcuts import render
from posts.models import all_posts
from .models import User_details
from django.contrib.auth.models import User, auth

# Create your views here.
def profile_details(request, id):
    user_posts = all_posts.objects.filter(user=id) 
    user_details = User.objects.filter(id=id)
    secondary_details = User_details.objects.filter(user=id) 
    return render(request, 'profile.html', {'user_posts': user_posts, 'user_details': user_details, 'secondary_details': secondary_details})