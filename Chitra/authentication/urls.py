from django.urls import path
from .views import login, signup, logout,reset_password

urlpatterns = [
    path('login', login),
    path('signup', signup),
    path('reset', reset_password),
    path('logout', logout)
]