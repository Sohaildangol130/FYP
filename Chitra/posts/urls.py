from django.urls import path
from .views import view_post
urlpatterns = [
    path('<int:id>', view_post)
]