from django.urls import path
from .views import profile_details
urlpatterns = [
    path('<int:id>', profile_details),
]