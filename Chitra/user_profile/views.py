from django.shortcuts import render, redirect
from posts.models import all_posts
from .models import User_details
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def profile_details(request, id):
    user_posts = all_posts.objects.filter(user=id) 
    user_details = User.objects.filter(id=id)
    secondary_details = User_details.objects.filter(user=id) 
    return render(request, 'profile.html', {'user_posts': user_posts, 'user_details': user_details, 'secondary_details': secondary_details})

def edit_profile(request, id):
    if (request.user.is_authenticated) and (request.user.id == id):
        user_details = User_details.objects.filter(user=id)
        return render(request, 'edit_profile.html', {'user_details': user_details})
    else:
        return redirect('/')

def primary_details(request, id):
    if (request.user.is_authenticated) and (request.user.id == id):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            user = User.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            messages.success(request, "Profile updated!! Please refresh the page to view the changes.")
            return redirect('/profile/edit/'+str(id))
        else:
            return redirect('/profile/edit/'+str(id))
    else:
        return redirect('/')

def user_image(request, id):
    if (request.user.is_authenticated) and (request.user.id == id):
        if request.method == 'POST' and request.FILES['user_image']:
            user_image = request.FILES['user_image']
            user = User_details.objects.get(user=id)
            user.profile_picture=user_image
            user.save()
            messages.success(request, "Profile updated!!")
            return redirect('/profile/edit/'+str(id))     
        else:
            return redirect('/profile/edit/'+str(id))
    else:
        return redirect('/')

def social_links(request, id):
    if (request.user.is_authenticated) and (request.user.id == id):
        if request.method == 'POST':
            facebook_link = request.POST['facebook-link']
            instagram_link = request.POST['instagram-link']
            behance_link = request.POST['behance-link']
            linkedin_link = request.POST['linkedin-link']

            user = User_details.objects.get(user=id)

            user.facebook_link=facebook_link
            user.instagram_link=instagram_link
            user.behance_link=behance_link
            user.linkedin_link=linkedin_link
            user.save()
            messages.success(request, "Social links updated!!")
            return redirect('/profile/edit/'+str(id))     
        else:
            return redirect('/profile/edit/'+str(id))
    else:
        return redirect('/')

def new_password(request, id):
    if (request.user.is_authenticated) and (request.user.id == id):
        if request.method == 'POST':
            password = request.POST['password']
            re_password = request.POST['repassword']
            if (password == re_password):
                user = User.objects.get(id=id)
                user.set_password(password)
                user.save()
                messages.success(request, "Profile updated!! Please log in again using your new password.")
                return redirect('/profile/edit/'+str(id))                
            else:
                messages.error(request, "Oops!! The passwords you've typed doesn't match.")
                return redirect('/profile/edit/'+str(id))
        else:
            return redirect('/profile/edit/'+str(id))
    else:
        return redirect('/')