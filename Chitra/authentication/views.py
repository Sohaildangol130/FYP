from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import random
# Create your views here.
def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=first_name).exists():
            print ("username taken")
        elif User.objects.filter(email=email).exists():
            print ("email taken")
        else:
            user = User.objects.create_user(username=first_name + str(random.randint(0,99999)), first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
        return redirect ('/')
    else:
        return render(request, 'register.html')
