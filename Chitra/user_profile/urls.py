from django.urls import path
from .views import profile_details, edit_profile, primary_details, new_password, user_image, social_links
urlpatterns = [
    path('<int:id>', profile_details),
    path('edit/<int:id>', edit_profile),
    path('edit/primary-details/<int:id>', primary_details),
    path('edit/user-image/<int:id>', user_image),
    path('edit/password/<int:id>', new_password),
    path('edit/social-links/<int:id>', social_links)
]