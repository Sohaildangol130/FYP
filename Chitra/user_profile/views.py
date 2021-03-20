from django.shortcuts import render
from posts.models import all_posts
# Create your views here.
def profile_details(request, id):
    user_posts = all_posts.objects.filter(user=id) 
    return render(request, 'profile.html', {'user_posts': user_posts})