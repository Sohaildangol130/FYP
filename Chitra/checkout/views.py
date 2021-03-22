from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from posts.models import all_posts
from django.contrib.auth.models import User

def checkout(request):
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