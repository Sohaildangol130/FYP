from django.urls import path
from .views import items_display,order

urlpatterns = [
    path('', order),
    path('show', items_display)
]