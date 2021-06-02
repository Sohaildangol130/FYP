from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from user_profile.models import User_details
import random, string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@csrf_exempt
def header(request):
    if (request.user.is_authenticated):
        user_details = User_details.objects.filter(user=int(request.POST.getlist('id')[0])).values_list()
        for i in user_details:
            user_image = i[2]
        return JsonResponse({'user_image': user_image}, safe=False)
    else:
        return JsonResponse("No authenticated user", safe=False)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            if (User.objects.get(email__exact=email)):
                user = auth.authenticate(username=User.objects.get(email__exact=email), password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "Email or password is incorrect.")
                    return render(request, 'login.html', {'title': "Login - Glad you're back!!"})         
        except ObjectDoesNotExist:
            messages.error(request, "User does not seem to exist. Please create an account.")
            return render(request, 'login.html', {'title': "Login - Glad you're back!!"})  
    else:
        return render(request, 'login.html', {'title': "Login - Glad you're back!!"})

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['re_password']        
        if (User.objects.filter(email=email).exists()):
            messages.error(request, email + " is already taken. Please try logging in with it.")
            return render(request, 'register.html')
        elif (password != repassword):
            messages.error(request, "The passwords do not match. Please try it again.")
            return render(request, 'register.html', {'title': 'Signup - Create, share, sell and grow as an artist.'})
        else:
            user = User.objects.create_user(username=first_name + str(random.randint(0,99999)), first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            user_detail = User.objects.get(email__exact=email)
            user_secondary = User_details(user=user_detail)
            user_secondary.save()
            user = auth.authenticate(username=user_detail.username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
    else:
        return render(request, 'register.html', {'title': 'Signup - Create, share, sell and grow as an artist.'})

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
            messages.success(request, "Please check your mail. We've sent a temporary password for you.")
            return redirect('/auth/login')
        else:
            messages.error(request, "Oops!! We don't have any account registered with " + email)
            return render(request, 'forget_password.html', {'title': "Login - Reset your account's password"})
    else:
        return render(request, 'forget_password.html', {'title': "Login - Reset your account's password"})

def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('items')
    auth.logout(request)
    messages.success(request, 'You have logged out successfully.')
    return response