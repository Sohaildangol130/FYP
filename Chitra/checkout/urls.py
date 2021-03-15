from django.urls import path
from .views import items_display

urlpatterns = [
    path('', items_display)
]