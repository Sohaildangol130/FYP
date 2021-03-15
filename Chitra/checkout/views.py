from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def items_display(request):
    print ("ajax")
    return JsonResponse("ajax")