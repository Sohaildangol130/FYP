from django.shortcuts import render, redirect
from .models import all_posts
from user_profile.models import User_details
# Create your views here.
def view_post(request, id):
    post = all_posts.objects.filter(id=id)
    for i in post:
        title = i.post_name
        user_details = User_details.objects.filter(user=i.user)
    return render (request, 'view_post.html', {'post': post, 'title': title, 'user_details': user_details})

def upload_post(request):
    if (request.user.is_authenticated):
        if request.method == 'POST' and request.FILES['image']:
            post_name = request.POST['post_name']
            description = request.POST['description']
            image = request.FILES['image']
            price = request.POST['price']
            if request.user.is_authenticated:
                if price !='':
                    user = request.user
                    post = all_posts(post_name=post_name, description=description, image=image, user=user, price=price)
                    post.save()
                    return redirect('/')   
                else:
                    user = request.user
                    post = all_posts(post_name=post_name, description=description, image=image, user=user)
                    post.save()
                    return redirect('/')  
        else:
            return render(request, 'upload_post.html', {'title': 'Upload your artwork'})
    else:
        return redirect('/')