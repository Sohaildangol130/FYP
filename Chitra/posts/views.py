from django.shortcuts import render, redirect
from .models import all_posts
from django.core.files.storage import FileSystemStorage

# Create your views here.
def view_post(request, id):
    pass

def upload_post(request):
    if request.method == 'POST' and request.FILES['image']:
        post_name = request.POST['post_name']
        description = request.POST['description']
        image = request.FILES['image']
        if request.user.is_authenticated:
            user = request.user
            post = all_posts(post_name=post_name, description=description, image=image, user=user)
            post.save()
            return redirect('/')
        
    else:
        return render(request, 'upload_post.html')