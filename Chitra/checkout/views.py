from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from posts.models import all_posts
@csrf_exempt
def items_display(request):
    if request.is_ajax and request.method == "POST":   
        checkout_posts = []  
        for i in request.POST.getlist('items[]'):
            posts = all_posts.objects.filter(id=int(i))
            post_query_list= posts.values_list()
            for i in post_query_list:
                post_details = {
                    'post_title': i[1],
                    'img_url': i[3]
                }
                checkout_posts.append(post_details)

        return JsonResponse({'checkout_posts': checkout_posts}, safe=False)