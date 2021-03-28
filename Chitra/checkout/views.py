from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from posts.models import all_posts
from .models import checkout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

def order(request):
    if request.method == 'POST':
        chars = "[]"
        posts = request.POST['posts']
        if (posts):
            phone_number = request.POST['phone_number']
            zone = request.POST['zone']
            city = request.POST['city']
            state = request.POST['state']
            zip_code = request.POST['zip_code']
            for c in chars:
                posts = posts.replace(c, '')
                products = posts.split(',')
            if request.user.is_authenticated:
                user = request.user
                for i in products:
                    product_details = all_posts.objects.get(id=int(i))
                    order = checkout(product=product_details, user=user, phone_number=phone_number, zone=zone, state=state, city=city, zip_code=zip_code )
                    order.save()
            response = HttpResponseRedirect('/')
            response.delete_cookie('items')
            messages.success(request, "Your order has been placed!!")
            return response
        else:
            messages.error(request, "Oops!! It seems there isn't any product to checkout.")
            return render(request, 'checkout.html')
    else:
        return render(request, 'checkout.html')

@csrf_exempt
def items_display(request):
    if request.is_ajax and request.method == "POST":   
        checkout_posts = []  
        for i in request.POST.getlist('items[]'):
            posts = all_posts.objects.filter(id=int(i))
            post_query_list= posts.values_list()
            for i in post_query_list:
                for j in User.objects.filter(id=i[4]).values_list():
                    post_details = {
                        'post_id': i[0],
                        'post_title': i[1],
                        'img_url': i[3],
                        'price': i[5],
                        'user': {
                            'id': j[0],
                            'first_name': j[5],
                            'last_name': j[6]
                        }
                    }
                checkout_posts.append(post_details)
        return JsonResponse({'checkout_posts': checkout_posts}, safe=False)