from django.shortcuts import render
from posts.models import all_posts
# Create your views here.
def index(request):
    post = all_posts.objects.all()
    return render(request, 'index.html', {'posts': post})