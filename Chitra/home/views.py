from django.shortcuts import render
from posts.models import all_posts
from django.contrib import messages

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
    # def get_context_data(self, **kwargs):
    #     title={'title': 'Chitra - Homepage'}
    #     return title

def search(request):
    search_text = request.GET['search']
    search_filter = all_posts.objects.filter(post_name__icontains=search_text)
    
    messages.info(request, "Related posts for " + search_text)
    return render(request, 'index.html', {'object_list': search_filter, 'title': 'Search results for ' + search_text})