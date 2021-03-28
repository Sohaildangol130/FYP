from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import random, string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if (User.objects.get(email__exact=email) ):
            user = auth.authenticate(username=User.objects.get(email__exact=email), password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Username or password is incorrect.")
                return render(request, 'login.html')         
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['re_password']
        
        if (User.objects.filter(email=email).exists()):
            messages.error(request, "The email is already taken. Please try logging in with it.")
            return render(request, 'register.html')
        elif (password != repassword):
            messages.error(request, "The passwords do not match. Please try it again.")
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=first_name + str(random.randint(0,99999)), first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
        return redirect ('/')
    else:
        return render(request, 'register.html')

def reset_password(request):
    if request.method == "POST":
        email = request.POST['email']
        if (User.objects.filter(email=email)):
            letters = string.ascii_uppercase
            new_password = ''.join(random.choice(letters) for i in range(10))
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            send_mail(
            'RESET PASSWORD',
            'Your new password: ' + new_password,
            'chitra.fyp@gmail.com',
            [email],
            fail_silently=False
            )
            messages.success(request, "Please check your email. We've sent a temporary password for you.")
            return redirect('/auth/login')
        else:
            messages.error(request, "Oops!! We don't have any account registered with that email.")
            return render(request, 'forget_password.html')

    else:
        return render(request, 'forget_password.html')

def logout(request):
    response = HttpResponseRedirect('/auth/login')
    response.delete_cookie('items')
    auth.logout(request)
    return response