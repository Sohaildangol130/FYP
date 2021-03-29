from django.urls import path
from .views import index, search

urlpatterns = [
    path('', index.as_view()),
    path('search', search)
]