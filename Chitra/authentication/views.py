from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import random
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=User.objects.get(email__exact=email), password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username or password is incorrect.")
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
            messages.info(request, "The email is already taken. Please try logging in with it.")
            return render(request, 'register.html')
        elif (password != repassword):
            messages.info(request, "The passwords do not match. Please try it again.")
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=first_name + str(random.randint(0,99999)), first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
        return redirect ('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
