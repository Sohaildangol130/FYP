from django.shortcuts import render
from posts.models import all_posts

from django.views.generic import (
    CreateView,
    DetailView,
    ListView, 
    UpdateView, 
    DetailView
)
# Create your views here.
class index(ListView):
    queryset = all_posts.objects.all()
    template_name = 'index.html'
