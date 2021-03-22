from django.urls import path
from .views import items_display,checkout

urlpatterns = [
    path('', checkout),
    path('show', items_display)
]